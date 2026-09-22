import { execFileSync } from "node:child_process";
import {
  existsSync,
  mkdtempSync,
  readFileSync,
  readdirSync,
  rmSync,
  statSync,
} from "node:fs";
import { tmpdir } from "node:os";
import path from "node:path";

const root = process.cwd();
const bufBin = path.join(root, "node_modules/.bin/buf");
const errors = [];

function fail(message) {
  errors.push(message);
}

function listFiles(dir, options = {}) {
  const files = [];
  for (const entry of readdirSync(dir).sort()) {
    const fullPath = path.join(dir, entry);
    const relativePath = path.relative(options.rootDir ?? dir, fullPath);
    if (options.ignore?.(relativePath, fullPath)) {
      continue;
    }
    const stat = statSync(fullPath);
    if (stat.isDirectory()) {
      files.push(
        ...listFiles(fullPath, { ...options, rootDir: options.rootDir ?? dir }),
      );
    } else if (stat.isFile()) {
      files.push(fullPath);
    }
  }
  return files;
}

function relativeFiles(dir, options = {}) {
  return listFiles(dir, { ...options, rootDir: dir })
    .map((filePath) => path.relative(dir, filePath))
    .sort();
}

function compareDirectories(actualDir, expectedDir, options = {}) {
  const actualFiles = relativeFiles(actualDir, options);
  const expectedFiles = relativeFiles(expectedDir, options);
  if (JSON.stringify(actualFiles) !== JSON.stringify(expectedFiles)) {
    fail(
      `${path.relative(root, expectedDir)} file list differs from fresh generation`,
    );
    return;
  }

  for (const relativePath of expectedFiles) {
    const actual = readFileSync(path.join(actualDir, relativePath));
    const expected = readFileSync(path.join(expectedDir, relativePath));
    if (!actual.equals(expected)) {
      fail(`${path.relative(root, expectedDir)}/${relativePath} is stale`);
    }
  }
}

function stripProtoComments(source) {
  return source.replace(/\/\/.*$/gm, "").replace(/\/\*[\s\S]*?\*\//g, "");
}

function parseProtoSurface(protoPath) {
  const source = stripProtoComments(readFileSync(protoPath, "utf8"));
  const messages = [];
  const enums = [];
  const messageRegex = /message\s+(\w+)\s*\{([\s\S]*?)\n\}/g;
  const enumRegex = /enum\s+(\w+)\s*\{/g;

  for (const match of source.matchAll(enumRegex)) {
    enums.push(match[1]);
  }

  for (const match of source.matchAll(messageRegex)) {
    const [, name, body] = match;
    const fields = [];
    const fieldRegex =
      /(?:optional\s+|repeated\s+)?(?:[\w.]+)\s+(\w+)\s*=\s*\d+\s*;/g;
    for (const fieldMatch of body.matchAll(fieldRegex)) {
      fields.push(fieldMatch[1]);
    }
    messages.push({ name, fields });
  }

  return { messages, enums };
}

function swiftFieldName(protoFieldName) {
  const parts = protoFieldName.split("_");
  return parts
    .map((part, index) => {
      if (index === 0) {
        return part;
      }
      if (part === "id") {
        return "ID";
      }
      return `${part[0].toUpperCase()}${part.slice(1)}`;
    })
    .join("");
}

function checkGeneratedSurface() {
  const protoFiles = relativeFiles(path.join(root, "proto")).filter(
    (fileName) => fileName.endsWith(".proto"),
  );
  const swiftFiles = new Set(relativeFiles(path.join(root, "gen/swift")));
  const pythonFiles = new Set(relativeFiles(path.join(root, "gen/python")));

  for (const protoFile of protoFiles) {
    const base = protoFile.replace(/\.proto$/, "");
    const expectedSwift = `${base}.pb.swift`;
    const expectedPython = `${base}_pb2.py`;
    const expectedPythonPyi = `${base}_pb2.pyi`;

    if (!swiftFiles.has(expectedSwift)) {
      fail(`missing Swift output for ${protoFile}: ${expectedSwift}`);
      continue;
    }
    if (!pythonFiles.has(expectedPython)) {
      fail(`missing Python output for ${protoFile}: ${expectedPython}`);
      continue;
    }
    if (!pythonFiles.has(expectedPythonPyi)) {
      fail(`missing Python type stub for ${protoFile}: ${expectedPythonPyi}`);
      continue;
    }

    const protoSurface = parseProtoSurface(path.join(root, "proto", protoFile));
    const swiftSource = readFileSync(
      path.join(root, "gen/swift", expectedSwift),
      "utf8",
    );
    const pythonPyiSource = readFileSync(
      path.join(root, "gen/python", expectedPythonPyi),
      "utf8",
    );

    for (const enumName of protoSurface.enums) {
      const swiftEnum = `enum Ensomi_Protocol_V1_${enumName}`;
      if (!swiftSource.includes(swiftEnum)) {
        fail(`Swift output missing enum ${enumName}`);
      }
      if (!pythonPyiSource.includes(`class ${enumName}(`)) {
        fail(`Python stub missing enum ${enumName}`);
      }
    }

    for (const message of protoSurface.messages) {
      const swiftStruct = `struct Ensomi_Protocol_V1_${message.name}`;
      if (!swiftSource.includes(swiftStruct)) {
        fail(`Swift output missing message ${message.name}`);
      }
      if (!pythonPyiSource.includes(`class ${message.name}(`)) {
        fail(`Python stub missing message ${message.name}`);
      }
      for (const fieldName of message.fields) {
        if (!pythonPyiSource.includes(`${fieldName}:`)) {
          fail(`Python stub missing field ${message.name}.${fieldName}`);
        }
        const swiftName = swiftFieldName(fieldName);
        if (!swiftSource.includes(`var ${swiftName}:`)) {
          fail(`Swift output missing field ${message.name}.${swiftName}`);
        }
      }
    }
  }
}

function checkPythonTypedMarker() {
  const markerPath = path.join(root, "gen/python/ensomi/protocol/py.typed");
  if (!existsSync(markerPath)) {
    fail("missing Python typed marker: gen/python/ensomi/protocol/py.typed");
  }
}

const tempDir = mkdtempSync(path.join(tmpdir(), "ensomi-protocol-gen-"));
try {
  execFileSync(bufBin, ["generate", "--output", tempDir], {
    cwd: root,
    stdio: "pipe",
  });
  compareDirectories(
    path.join(tempDir, "gen/swift"),
    path.join(root, "gen/swift"),
  );
  compareDirectories(
    path.join(tempDir, "gen/python"),
    path.join(root, "gen/python"),
    {
      ignore: (relativePath) =>
        relativePath === "ensomi/protocol/py.typed" ||
        relativePath.includes(".egg-info") ||
        relativePath.includes("__pycache__"),
    },
  );
} finally {
  rmSync(tempDir, { force: true, recursive: true });
}

checkGeneratedSurface();
checkPythonTypedMarker();

if (errors.length) {
  for (const error of errors) {
    console.error(error);
  }
  process.exit(1);
}

console.log(
  "generated Swift/Python outputs match proto and fresh Buf generation",
);

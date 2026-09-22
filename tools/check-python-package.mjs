import { execFileSync } from "node:child_process";
import { existsSync, mkdtempSync, readdirSync, rmSync } from "node:fs";
import { tmpdir } from "node:os";
import path from "node:path";

const root = process.cwd();
const tempDir = mkdtempSync(path.join(tmpdir(), "ensomi-protocol-python-"));
const rootBuildDir = path.join(root, "build");
const eggInfoDir = path.join(root, "gen/python/ensomi_protocol.egg-info");
const rootBuildDirExisted = existsSync(rootBuildDir);
const eggInfoDirExisted = existsSync(eggInfoDir);

function venvPython(venvDir) {
  if (process.platform === "win32") {
    return path.join(venvDir, "Scripts", "python.exe");
  }
  return path.join(venvDir, "bin", "python");
}

function run(command, args, options = {}) {
  execFileSync(command, args, {
    cwd: root,
    stdio: "inherit",
    ...options,
  });
}

try {
  const buildVenv = path.join(tempDir, "build-venv");
  const installVenv = path.join(tempDir, "install-venv");
  const distDir = path.join(tempDir, "dist");

  run("python3", ["-m", "venv", buildVenv]);
  const buildPython = venvPython(buildVenv);
  run(buildPython, ["-m", "pip", "install", "--upgrade", "pip", "build"]);
  run(buildPython, ["-m", "build", "--sdist", "--wheel", "--outdir", distDir]);

  const wheel = readdirSync(distDir).find((fileName) =>
    fileName.endsWith(".whl"),
  );
  if (!wheel) {
    throw new Error("python build did not produce a wheel");
  }

  run("python3", ["-m", "venv", installVenv]);
  const installPython = venvPython(installVenv);
  run(installPython, ["-m", "pip", "install", "--upgrade", "pip"]);
  run(installPython, ["-m", "pip", "install", path.join(distDir, wheel)]);
  run(installPython, [
    "-c",
    "from ensomi.protocol.v1 import envelope_pb2; envelope_pb2.Envelope(session_id='wheel')",
  ]);

  console.log("python wheel builds, installs, and imports");
} finally {
  rmSync(tempDir, { force: true, recursive: true });
  if (!rootBuildDirExisted) {
    rmSync(rootBuildDir, { force: true, recursive: true });
  }
  if (!eggInfoDirExisted) {
    rmSync(eggInfoDir, { force: true, recursive: true });
  }
}

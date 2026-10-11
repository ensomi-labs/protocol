# Model package

A model package is a directory of files published together, for example the `onnx/` directory of
`sed-i/ensomi-r2` at Hugging Face. `model_package.proto` defines the manifest that describes it.

## Layout

- The manifest is the proto3 JSON encoding of `ModelPackageManifest` in a file named `ensomi-model.json` at
  the root of the package directory. In that encoding 64-bit integers such as `sizeBytes` are decimal
  strings.
- `ModelPackageManifest.files` lists every other file of the package, with `path` relative to the directory
  that holds the manifest, `size_bytes` and `sha256_hex`. The manifest does not list itself.
- Each entry of `graphs` names an ONNX file from `files` with the opset it was exported with. The file at
  `runtime_config_path` (`runtime.json` for R2) configures the runtime for those graphs.

## What a client does

1. Download `ensomi-model.json`.
2. Check that its own runtime version lies in `runtime_versions` and that it accepts `license`. If not,
   stop before downloading weights.
3. Download each file, and check its size and SHA-256 against the manifest. Reject the package on any
   mismatch; never load a file that failed.
4. Load the graphs by `name` with an ONNX Runtime that supports each `opset`, and pass the runtime config
   to the runtime.

A model service reports the same `model_name`, `model_version` and `files` in `ModelCapabilities`, so a
client can tell that a chart came from the package it holds.

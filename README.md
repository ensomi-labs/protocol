# Ensomi Protocol

Shared protocol package for projects under [github.com/ensomi-labs](https://github.com/ensomi-labs).

## Repository Layout

```text
proto/              Protocol Buffers source of truth.
gen/swift/          Generated SwiftProtobuf code, committed and shipped.
gen/python/         Generated Python protobuf code and type stubs, committed and shipped.
docs/               Protocol notes shipped with the npm package.
tools/              Local generation and drift-check scripts.
Package.swift       SwiftPM manifest for Swift/Xcode consumers.
pyproject.toml      Python package metadata for wheel/sdist consumers.
buf.yaml            Proto lint and breaking-change configuration.
buf.gen.yaml        Swift and Python generation configuration.
```

The Swift app and Python model consume generated code from `gen/`. The `.proto` files remain the protocol source of truth. WebSocket payloads should be binary protobuf `Envelope` messages. JSON is reserved for debug and logs.

See [Protocol Guidelines](./PROTOCOL_GUIDELINES.md) for schema evolution, naming, and comment conventions. See [Session Scope](./docs/session-scope.md) for `Envelope.session_id` requirements by payload.

The v1 protobuf source is split by responsibility:

```text
proto/ensomi/protocol/v1/core.proto
  Node identity, roles, and advertised capabilities.

proto/ensomi/protocol/v1/envelope.proto
  Transport envelope, routing metadata, correlation ids, and payload union.

proto/ensomi/protocol/v1/inference.proto
  Inference requests, lifecycle status, errors, and end-of-stream events.

proto/ensomi/protocol/v1/mapper.proto
  Opaque mapper token events.
```

## Current Scope

This package owns the stable cross-language contract between Ensomi clients, the Python model endpoint, and npm consumers:

- Node graph identity for host, player client, model service, hardware, and debug-tool processes.
- Inference WebSocket envelopes: ready, audio, reference time, stop, status, error, hitobject token, and end-of-stream.
- Opaque mapper token stream events tagged with a token-contract version.

This package does not own token decoding, decoded Mania4K/domain state, model inference internals, Torch checkpoints, timing fitting algorithms, SwiftUI state, rendering, judgement, input routing, audio clock implementations, or full `.osu` parsing/export.

## Distribution Surfaces

This repository publishes the same protocol contract through multiple language-native surfaces. Downstream Swift and Python projects do not need their own `package.json`.

### npm

The npm package remains useful for Node tooling, registry-backed tarballs, and consumers that want direct access to `proto/` and `gen/`:

```sh
npm install @ensomi/protocol
```

### SwiftPM

Swift/Xcode consumers should depend on this Git repository directly:

```swift
.package(
    url: "https://github.com/ensomi-labs/protocol.git",
    from: "0.1.0"
)
```

Then add the product to a target:

```swift
.product(name: "EnsomiProtocol", package: "protocol")
```

SwiftPM publication is Git-tag based. Create and push a semver tag such as `0.1.0`; no central Swift registry is required for this bootstrap path.

### Python

Python consumers should eventually use the PyPI package:

```sh
pip install ensomi-protocol==0.1.0
```

The local bootstrap build is:

```sh
python3 -m pip install build
python3 -m build --sdist --wheel --outdir dist/
python3 -m pip install dist/*.whl
python3 -c "from ensomi.protocol.v1 import envelope_pb2; envelope_pb2.Envelope()"
```

Generated Python classes live in the module for their source `.proto` file. For example, import `Envelope` from `envelope_pb2`, inference messages from `inference_pb2`, mapper token messages from `mapper_pb2`, and node graph messages from `core_pb2`.

The `Publish Python package` GitHub workflow is manual and expects PyPI trusted publishing to be configured for the repository/environment before it is run.

## Development Tools

- Node.js package manager: `npm@11.12.1`, recorded in `package.json`.
- Runtime floor: Node.js `>=22.0.0`.
- Protobuf workflow: local npm binaries, not global installs.
- Proto lint/generation: `@bufbuild/buf`.
- Swift generation: Buf remote plugin `buf.build/apple/swift`.
- Python generation: Buf remote plugins `buf.build/protocolbuffers/python` and `buf.build/protocolbuffers/pyi`.
- Formatting: `prettier`.

## Commands

```sh
npm run generate
npm run proto:lint
npm run proto:generate
npm run generated:check
npm run check
npm run python:check
npm run swift:build
npm run bootstrap:check
```

`npm run generated:check` regenerates Swift and Python outputs in a temporary directory and compares them byte-for-byte with `gen/`. It also verifies that the generated Python stubs and Swift file expose the same message, enum, and field surface declared by the proto.

## License

Licensed under the Apache License, Version 2.0. See [LICENSE](./LICENSE).

# @ensomi/protocol

## 0.3.0 (unreleased)

### Minor Changes

- Add the chart stream in `chart_stream.proto`: `ChartStreamRequest`, `ChartStreamOpened`, `ChartPageRequest` (`after_sequence`, `through_ms`) and `ChartPage` (`sequence`, `coverage_ms`, `end_of_stream`, `ChartObject`s, receipt). The four messages join `Envelope.payload` at field numbers 29 to 32. It replaces the JSON `ensomi-demo/v1` contract.
- Additive: no existing message, field number or enum value changed.

### Patch Changes

- The Python package requires `protobuf>=5.26.1,<9` instead of `<6`. Its gencode (Buf plugins `protocolbuffers/python` and `pyi` v26.1) is supported on protobuf runtimes 5.26.1 through 8.x by protobuf's [cross-version runtime guarantee](https://protobuf.dev/support/cross-version-runtime-guarantee/), so it installs beside packages that need protobuf 6 or 7, such as onnx 1.23.
- `chart.proto` documents the `ErrorEvent.code` `protocol_error` (PROTOCOL_ERROR): a frame the chart service cannot parse or handle, or one that breaks the session flow, such as a request without a session id or a second request in a generating session. The model service already sent it. Comments only; generated code is unchanged.

## 0.2.0

### Minor Changes

- Add complete-chart generation in `chart.proto`: `GenerateChartRequest` (audio, star, seed, long-note amount and section requests), `CapabilitiesRequest` / `ModelCapabilities`, `GenerationProgress` and `ChartResult` (the chart as `{lane, start_ms, end_ms?}` objects plus a receipt). The five messages join `Envelope.payload` at field numbers 24 to 28. Additive: no existing message or field number changed.

## 0.1.0

### Minor Changes

- 5bcb7fd: Migrate the package, protobuf namespaces, generated bindings, documentation, and repository metadata to Ensomi naming.

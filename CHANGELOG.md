# @ensomi/protocol

## 0.2.0

### Minor Changes

- Add complete-chart generation in `chart.proto`: `GenerateChartRequest` (audio, star, seed, long-note amount and section requests), `CapabilitiesRequest` / `ModelCapabilities`, `GenerationProgress` and `ChartResult` (the chart as `{lane, start_ms, end_ms?}` objects plus a receipt). The five messages join `Envelope.payload` at field numbers 24 to 28. Additive: no existing message or field number changed.

## 0.1.0

### Minor Changes

- 5bcb7fd: Migrate the package, protobuf namespaces, generated bindings, documentation, and repository metadata to Ensomi naming.

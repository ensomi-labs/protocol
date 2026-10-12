# @ensomi/protocol

## 0.3.0 (unreleased)

### Minor Changes

- Add the chart stream in `chart_stream.proto`: `ChartStreamRequest`, `ChartStreamOpened`, `ChartPageRequest` (`after_sequence`, `through_ms`) and `ChartPage` (`sequence`, `coverage_ms`, `end_of_stream`, `ChartObject`s, receipt). The four messages join `Envelope.payload` at field numbers 29 to 32. It replaces the JSON `ensomi-demo/v1` contract.
- Additive: no existing message, field number or enum value changed.

## 0.2.0

### Minor Changes

- Add complete-chart generation in `chart.proto`: `GenerateChartRequest` (audio, star, seed, long-note amount and section requests), `CapabilitiesRequest` / `ModelCapabilities`, `GenerationProgress` and `ChartResult` (the chart as `{lane, start_ms, end_ms?}` objects plus a receipt). The five messages join `Envelope.payload` at field numbers 24 to 28. Additive: no existing message or field number changed.

## 0.1.0

### Minor Changes

- 5bcb7fd: Migrate the package, protobuf namespaces, generated bindings, documentation, and repository metadata to Ensomi naming.

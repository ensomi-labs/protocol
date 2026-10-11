# Session Scope

`Envelope.session_id` defines the session scope for the envelope payload. Payload
messages do not duplicate `session_id`; receivers validate the payload against the
session id carried by the envelope.

## Rules

| Payload                | `Envelope.session_id`                                                                     |
| ---------------------- | ----------------------------------------------------------------------------------------- |
| `NodeHello`            | MUST be empty                                                                             |
| `ReadyRequest`         | SHOULD be empty                                                                           |
| `AudioRequest`         | MUST be non-empty                                                                         |
| `ReferenceTimeRequest` | MUST be non-empty                                                                         |
| `HitObjectTokenEvent`  | MUST be non-empty                                                                         |
| `StopSessionRequest`   | MUST be non-empty                                                                         |
| `GenerateChartRequest` | MUST be non-empty                                                                         |
| `GenerationProgress`   | MUST be non-empty, the request's session                                                  |
| `ChartResult`          | MUST be non-empty, the request's session                                                  |
| `ChartStreamRequest`   | MUST be non-empty                                                                         |
| `ChartStreamOpened`    | MUST be non-empty, the request's session                                                  |
| `ChartPageRequest`     | MUST be non-empty, the stream's session                                                   |
| `ChartPage`            | MUST be non-empty, the stream's session                                                   |
| `CapabilitiesRequest`  | SHOULD be empty                                                                           |
| `ModelCapabilities`    | SHOULD be empty                                                                           |
| `StatusEvent`          | MAY be empty for endpoint/node-scoped status; MUST be non-empty for session-scoped status |

`Replay`, `PlayResult` and `ModelPackageManifest` are documents, not `Envelope` payloads, and have no
session scope.

`StopSessionRequest` intentionally has no `session_id` field. It targets the
active session identified by `Envelope.session_id`; therefore an envelope with
`payload.stop_session` and an empty `Envelope.session_id` is invalid.

`StatusEvent` is the only payload in this list that can validly cross the
session boundary. Endpoint-level statuses such as cold startup or readiness can
use an empty `Envelope.session_id`. Statuses describing an active session, a
missing session, or a session transition use the relevant non-empty
`Envelope.session_id`.

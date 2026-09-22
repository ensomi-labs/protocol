# Protocol Guidelines

## Intent

This package defines the shared protobuf contract for Ensomi clients and model services. The goal is to keep the protocol easy to evolve while avoiding accidental wire-format breakage.

## Change Policy

During early `0.x` development, breaking changes are allowed when all known consumers are updated in the same release.

Once the protocol is used by independently updated clients, prefer additive changes:

- Add new fields with fresh numbers.
- Add new enum values with fresh numbers.
- Add new `Envelope.payload` variants with fresh numbers.

Avoid reusing field numbers from published schemas. If a field was removed after publication, reserve its old number and name when practical.

Moving a message to another `.proto` file can preserve its fully qualified protobuf type name and binary wire compatibility, but it changes generated module/file boundaries in languages such as Python. Treat those moves as generated API breaks during `0.x`, document the import migration, and update known consumers in the same release.

## Source Of Truth

- `.proto` files under `proto/` are the source of truth.
- Keep transport, graph/core vocabulary, inference, and opaque mapper token events in separate source files when the concepts can evolve independently.
- Breaking-change checks use package-level compatibility so source files can be reorganized without treating stable fully qualified type moves as wire breaks.
- Generated code under `gen/` is committed for Swift/Python consumers.
- WebSocket payloads should use binary protobuf `Envelope`.

## Responsibility Boundary

This package should contain stable, cross-process protocol contracts:

- Node graph identity, roles, and capability announcements for host, player client, model service, hardware, and debug-tool processes.
- Inference endpoint messages and lifecycle states.
- Machine-readable enums and error codes shared by Swift, Python, and npm consumers.
- Opaque token-stream events tagged with the token-contract version needed by Swift/model-side decoders.
- Generated artifacts that prove those contracts are stable.

Keep implementation details in their owning repositories:

- Model training, Torch runtime, checkpoint loading, mel/control features, grammar decoding, and timing fitting algorithms stay in `Ensomi-model`.
- Token decoding, decoded Mania4K/domain state, SwiftUI view state, AVFoundation clocks, input routing, rendering, judgement, scoring, and local-library/recognition integrations stay in `Ensomi`.
- Full `.osu` import/export behavior stays outside this protocol.

## Inference Lifecycle

The v1 endpoint lifecycle is:

```text
ready -> audio_preparing -> audio_ready -> streaming -> stopped
                                      \-> failed
```

Use `StatusEvent` when a service sends lifecycle transitions over the protocol. The current model endpoint logs `ws_status`; new protobuf consumers should prefer `StatusEvent`.

## Token Contract

The protobuf layer treats mapper tokens as opaque ids plus `token_contract_version`. Token decoding tables, lane actions, quantization rules, and reducer/domain state belong in the Swift and model repositories that share the token-stream transport definitions.

## Comments

Comments should explain protocol meaning, not restate the field name.

Add comments when:

- A message represents a wire-level event or request.
- A field has units, clock source, ordering semantics, or lifecycle assumptions.
- A field is optional and absence has a distinct meaning.
- An enum value is non-obvious.
- A value is experimental or temporary.
- A field exists for compatibility with a specific consumer.

Prefer comments like:

```proto
// Sent by the client to request beatmap inference for an audio source.
message AudioRequest {
  // Local or sandbox-relative path understood by the receiving model service.
  string audio_path = 1;

  // Duration of the selected audio in milliseconds, when known by the client.
  optional uint32 audio_length_ms = 2;
}
```

Avoid comments like:

```proto
// The audio path.
string audio_path = 1;
```

## Naming And Units

- Use `snake_case` field names.
- Include units in names when they clarify meaning, such as `_ms`, `_unix_ms`, `_count`, or `_id`.
- Use `*_UNSPECIFIED = 0` for enum defaults.
- Prefer enums for machine-readable state.
- Use strings for human-facing or debug messages.

## Validation

The schema defines shape. Runtime code still validates behavior:

- Payload is present.
- `session_id` is known.
- `sequence` ordering is acceptable.
- Time values are in expected ranges.
- State transitions make sense.

## Workflow

Use local npm scripts:

```sh
npm run generate
npm run proto:format
npm run proto:lint
npm run generated:check
npm run check
```

Generated Swift/Python files must be updated in the same change as proto edits. `npm run generated:check` compares committed outputs with fresh Buf generation and checks that Python stubs and Swift generated code expose the same proto surface.

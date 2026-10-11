# Gameplay

`gameplay.proto` defines the data of a mania 4K play: `Ruleset`, `InputEvent`, `Replay` and `PlayResult`.
The judgement itself runs in the shared Ensomi runtime and in clients that have not moved to it yet. This
page fixes what they must agree on.

**A result depends on the chart, the ruleset and the inputs only.** It does not depend on how often a
client advances its clock, on the client, or on the runtime build. Judging a `Replay` against the chart its
`ChartIdentity` names gives the same `PlayResult` everywhere. `Ruleset.rules_version` names the rules below;
a change to them takes a new version.

## Time

- `ChartObject` times are audio milliseconds, unshifted.
- `InputEvent.chart_time_ms` is gameplay chart time: `audio time + Replay.audio_offset_ms`. Judgement reads
  it as is. `Replay.visual_offset_ms` moves notes on screen and never reaches judgement.
- Hit error is `input time - object time`: positive when late.

## Chart identity

`ChartIdentity.sha256_hex` is the SHA-256 of the binary `Chart` that was played, serialized with fields in
ascending field-number order. Generated code in every language emits that order. A replay does not carry
the chart: a reader fetches or regenerates it and compares the hash before judging.

## Evaluation (rules version 1)

Objects come from `Chart.objects`: a tap, or a hold with a head at `start_ms` and a release at `end_ms`.
Each object is judged once. Process `Replay.inputs` in list order. Before each input at time `t`, and once
at the end with `t = +infinity`, advance to `t`; this makes every result independent of when a client
happened to advance during live play.

**Advance to `t`:**

1. In each lane, the earliest unresolved object is missed while the next unresolved object of that lane
   starts at or before `t` (note lock). Repeat until none is.
2. A waiting object (head not yet pressed) is missed when `t > start_ms + g_ms`.
3. A held hold is missed when `t > end_ms + g_ms * tail_multiplier`.

**Press in a lane at `t`:** the target is the lane's earliest waiting object; with none, the press is
ignored. With hit error `e = t - start_ms`: if `e < -g_ms` the press is ignored (too early, not a miss).
Otherwise the tier is the best whose half-window is at least `|e|`, or M when `|e| > g_ms`. A tap resolves
at that tier. A hold resolves as M if the tier is M; otherwise it is held, remembering the head tier and `e`.

**Release in a lane at `t`:** the target is the lane's held hold; with none, the release is ignored. The
hold resolves as M if `t < end_ms - g_ms * tail_multiplier`. Otherwise the release tier is the best whose
half-window times `tail_multiplier` is at least `|t - end_ms|`, or M beyond `g_ms * tail_multiplier`. The
hold resolves at the worse of the head tier and the release tier.

**Result:** every resolution adds one to its tier count. A tier better than M adds one to the combo and a
miss resets it; `max_combo` is the highest combo reached, counting in the order objects resolved. For each
object resolved better than M, its head's hit error `e` is a sample; `suggested_audio_offset_adjustment_ms`
is minus the mean of the samples, absent without samples. `accuracy` is the weighted mean in `PlayResult`,
1 for an empty chart.

A live client reaches the same result when it advances to each input's time before handling the input, as
the loop above does.

## Presets

`Ruleset.windows` always carries the windows in force. The presets A to E are tabulated on
`JudgeDifficulty`; a client building a ruleset from a preset copies that row.

## Stored plays

`Replay` and `PlayResult` are documents. Store a replay as a file or send it in an HTTP body, in binary
protobuf or in the proto3 JSON mapping. They are not `Envelope` payloads.

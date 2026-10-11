from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class JudgementTier(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    JUDGEMENT_TIER_UNSPECIFIED: _ClassVar[JudgementTier]
    JUDGEMENT_TIER_BIG_P: _ClassVar[JudgementTier]
    JUDGEMENT_TIER_P1: _ClassVar[JudgementTier]
    JUDGEMENT_TIER_P2: _ClassVar[JudgementTier]
    JUDGEMENT_TIER_P3: _ClassVar[JudgementTier]
    JUDGEMENT_TIER_G: _ClassVar[JudgementTier]
    JUDGEMENT_TIER_M: _ClassVar[JudgementTier]

class JudgeDifficulty(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    JUDGE_DIFFICULTY_UNSPECIFIED: _ClassVar[JudgeDifficulty]
    JUDGE_DIFFICULTY_A: _ClassVar[JudgeDifficulty]
    JUDGE_DIFFICULTY_B: _ClassVar[JudgeDifficulty]
    JUDGE_DIFFICULTY_C: _ClassVar[JudgeDifficulty]
    JUDGE_DIFFICULTY_D: _ClassVar[JudgeDifficulty]
    JUDGE_DIFFICULTY_E: _ClassVar[JudgeDifficulty]

class InputPhase(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    INPUT_PHASE_UNSPECIFIED: _ClassVar[InputPhase]
    INPUT_PHASE_PRESS: _ClassVar[InputPhase]
    INPUT_PHASE_RELEASE: _ClassVar[InputPhase]

class ClientPlatform(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CLIENT_PLATFORM_UNSPECIFIED: _ClassVar[ClientPlatform]
    CLIENT_PLATFORM_MACOS: _ClassVar[ClientPlatform]
    CLIENT_PLATFORM_IOS: _ClassVar[ClientPlatform]
    CLIENT_PLATFORM_ANDROID: _ClassVar[ClientPlatform]
    CLIENT_PLATFORM_WINDOWS: _ClassVar[ClientPlatform]
    CLIENT_PLATFORM_WEB: _ClassVar[ClientPlatform]
JUDGEMENT_TIER_UNSPECIFIED: JudgementTier
JUDGEMENT_TIER_BIG_P: JudgementTier
JUDGEMENT_TIER_P1: JudgementTier
JUDGEMENT_TIER_P2: JudgementTier
JUDGEMENT_TIER_P3: JudgementTier
JUDGEMENT_TIER_G: JudgementTier
JUDGEMENT_TIER_M: JudgementTier
JUDGE_DIFFICULTY_UNSPECIFIED: JudgeDifficulty
JUDGE_DIFFICULTY_A: JudgeDifficulty
JUDGE_DIFFICULTY_B: JudgeDifficulty
JUDGE_DIFFICULTY_C: JudgeDifficulty
JUDGE_DIFFICULTY_D: JudgeDifficulty
JUDGE_DIFFICULTY_E: JudgeDifficulty
INPUT_PHASE_UNSPECIFIED: InputPhase
INPUT_PHASE_PRESS: InputPhase
INPUT_PHASE_RELEASE: InputPhase
CLIENT_PLATFORM_UNSPECIFIED: ClientPlatform
CLIENT_PLATFORM_MACOS: ClientPlatform
CLIENT_PLATFORM_IOS: ClientPlatform
CLIENT_PLATFORM_ANDROID: ClientPlatform
CLIENT_PLATFORM_WINDOWS: ClientPlatform
CLIENT_PLATFORM_WEB: ClientPlatform

class JudgementWindows(_message.Message):
    __slots__ = ("big_p_ms", "p1_ms", "p2_ms", "p3_ms", "g_ms", "tail_multiplier")
    BIG_P_MS_FIELD_NUMBER: _ClassVar[int]
    P1_MS_FIELD_NUMBER: _ClassVar[int]
    P2_MS_FIELD_NUMBER: _ClassVar[int]
    P3_MS_FIELD_NUMBER: _ClassVar[int]
    G_MS_FIELD_NUMBER: _ClassVar[int]
    TAIL_MULTIPLIER_FIELD_NUMBER: _ClassVar[int]
    big_p_ms: float
    p1_ms: float
    p2_ms: float
    p3_ms: float
    g_ms: float
    tail_multiplier: float
    def __init__(self, big_p_ms: _Optional[float] = ..., p1_ms: _Optional[float] = ..., p2_ms: _Optional[float] = ..., p3_ms: _Optional[float] = ..., g_ms: _Optional[float] = ..., tail_multiplier: _Optional[float] = ...) -> None: ...

class Ruleset(_message.Message):
    __slots__ = ("difficulty", "windows", "rules_version")
    DIFFICULTY_FIELD_NUMBER: _ClassVar[int]
    WINDOWS_FIELD_NUMBER: _ClassVar[int]
    RULES_VERSION_FIELD_NUMBER: _ClassVar[int]
    difficulty: JudgeDifficulty
    windows: JudgementWindows
    rules_version: int
    def __init__(self, difficulty: _Optional[_Union[JudgeDifficulty, str]] = ..., windows: _Optional[_Union[JudgementWindows, _Mapping]] = ..., rules_version: _Optional[int] = ...) -> None: ...

class InputEvent(_message.Message):
    __slots__ = ("lane", "phase", "chart_time_ms")
    LANE_FIELD_NUMBER: _ClassVar[int]
    PHASE_FIELD_NUMBER: _ClassVar[int]
    CHART_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    lane: int
    phase: InputPhase
    chart_time_ms: float
    def __init__(self, lane: _Optional[int] = ..., phase: _Optional[_Union[InputPhase, str]] = ..., chart_time_ms: _Optional[float] = ...) -> None: ...

class ChartIdentity(_message.Message):
    __slots__ = ("sha256_hex", "audio_sha256_hex", "title", "artist")
    SHA256_HEX_FIELD_NUMBER: _ClassVar[int]
    AUDIO_SHA256_HEX_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    ARTIST_FIELD_NUMBER: _ClassVar[int]
    sha256_hex: str
    audio_sha256_hex: str
    title: str
    artist: str
    def __init__(self, sha256_hex: _Optional[str] = ..., audio_sha256_hex: _Optional[str] = ..., title: _Optional[str] = ..., artist: _Optional[str] = ...) -> None: ...

class ClientIdentity(_message.Message):
    __slots__ = ("app_id", "app_version", "platform")
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    APP_VERSION_FIELD_NUMBER: _ClassVar[int]
    PLATFORM_FIELD_NUMBER: _ClassVar[int]
    app_id: str
    app_version: str
    platform: ClientPlatform
    def __init__(self, app_id: _Optional[str] = ..., app_version: _Optional[str] = ..., platform: _Optional[_Union[ClientPlatform, str]] = ...) -> None: ...

class RuntimeIdentity(_message.Message):
    __slots__ = ("version",)
    VERSION_FIELD_NUMBER: _ClassVar[int]
    version: str
    def __init__(self, version: _Optional[str] = ...) -> None: ...

class Replay(_message.Message):
    __slots__ = ("chart", "ruleset", "audio_offset_ms", "visual_offset_ms", "inputs", "client", "runtime")
    CHART_FIELD_NUMBER: _ClassVar[int]
    RULESET_FIELD_NUMBER: _ClassVar[int]
    AUDIO_OFFSET_MS_FIELD_NUMBER: _ClassVar[int]
    VISUAL_OFFSET_MS_FIELD_NUMBER: _ClassVar[int]
    INPUTS_FIELD_NUMBER: _ClassVar[int]
    CLIENT_FIELD_NUMBER: _ClassVar[int]
    RUNTIME_FIELD_NUMBER: _ClassVar[int]
    chart: ChartIdentity
    ruleset: Ruleset
    audio_offset_ms: float
    visual_offset_ms: float
    inputs: _containers.RepeatedCompositeFieldContainer[InputEvent]
    client: ClientIdentity
    runtime: RuntimeIdentity
    def __init__(self, chart: _Optional[_Union[ChartIdentity, _Mapping]] = ..., ruleset: _Optional[_Union[Ruleset, _Mapping]] = ..., audio_offset_ms: _Optional[float] = ..., visual_offset_ms: _Optional[float] = ..., inputs: _Optional[_Iterable[_Union[InputEvent, _Mapping]]] = ..., client: _Optional[_Union[ClientIdentity, _Mapping]] = ..., runtime: _Optional[_Union[RuntimeIdentity, _Mapping]] = ...) -> None: ...

class TierCounts(_message.Message):
    __slots__ = ("big_p_count", "p1_count", "p2_count", "p3_count", "g_count", "m_count")
    BIG_P_COUNT_FIELD_NUMBER: _ClassVar[int]
    P1_COUNT_FIELD_NUMBER: _ClassVar[int]
    P2_COUNT_FIELD_NUMBER: _ClassVar[int]
    P3_COUNT_FIELD_NUMBER: _ClassVar[int]
    G_COUNT_FIELD_NUMBER: _ClassVar[int]
    M_COUNT_FIELD_NUMBER: _ClassVar[int]
    big_p_count: int
    p1_count: int
    p2_count: int
    p3_count: int
    g_count: int
    m_count: int
    def __init__(self, big_p_count: _Optional[int] = ..., p1_count: _Optional[int] = ..., p2_count: _Optional[int] = ..., p3_count: _Optional[int] = ..., g_count: _Optional[int] = ..., m_count: _Optional[int] = ...) -> None: ...

class PlayResult(_message.Message):
    __slots__ = ("tier_counts", "accuracy", "max_combo", "suggested_audio_offset_adjustment_ms")
    TIER_COUNTS_FIELD_NUMBER: _ClassVar[int]
    ACCURACY_FIELD_NUMBER: _ClassVar[int]
    MAX_COMBO_FIELD_NUMBER: _ClassVar[int]
    SUGGESTED_AUDIO_OFFSET_ADJUSTMENT_MS_FIELD_NUMBER: _ClassVar[int]
    tier_counts: TierCounts
    accuracy: float
    max_combo: int
    suggested_audio_offset_adjustment_ms: float
    def __init__(self, tier_counts: _Optional[_Union[TierCounts, _Mapping]] = ..., accuracy: _Optional[float] = ..., max_combo: _Optional[int] = ..., suggested_audio_offset_adjustment_ms: _Optional[float] = ...) -> None: ...

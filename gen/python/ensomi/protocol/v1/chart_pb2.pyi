from ensomi.protocol.v1 import inference_pb2 as _inference_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LongNoteAmount(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    LONG_NOTE_AMOUNT_UNSPECIFIED: _ClassVar[LongNoteAmount]
    LONG_NOTE_AMOUNT_TAP_ONLY: _ClassVar[LongNoteAmount]
    LONG_NOTE_AMOUNT_HALF: _ClassVar[LongNoteAmount]
    LONG_NOTE_AMOUNT_NATURAL: _ClassVar[LongNoteAmount]

class PatternKind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PATTERN_KIND_UNSPECIFIED: _ClassVar[PatternKind]
    PATTERN_KIND_STREAM: _ClassVar[PatternKind]
    PATTERN_KIND_JUMPSTREAM: _ClassVar[PatternKind]
    PATTERN_KIND_CHORDSTREAM: _ClassVar[PatternKind]
    PATTERN_KIND_JACK: _ClassVar[PatternKind]
    PATTERN_KIND_CHORDJACK: _ClassVar[PatternKind]

class ControlStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CONTROL_STATUS_UNSPECIFIED: _ClassVar[ControlStatus]
    CONTROL_STATUS_WORKS: _ClassVar[ControlStatus]
    CONTROL_STATUS_EXPERIMENTAL: _ClassVar[ControlStatus]
    CONTROL_STATUS_NOT_WORKING: _ClassVar[ControlStatus]

class GenerationPhase(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    GENERATION_PHASE_UNSPECIFIED: _ClassVar[GenerationPhase]
    GENERATION_PHASE_LOADING: _ClassVar[GenerationPhase]
    GENERATION_PHASE_TIMING: _ClassVar[GenerationPhase]
    GENERATION_PHASE_ROWS: _ClassVar[GenerationPhase]
    GENERATION_PHASE_ARRANGEMENT: _ClassVar[GenerationPhase]
    GENERATION_PHASE_EXPORT: _ClassVar[GenerationPhase]
LONG_NOTE_AMOUNT_UNSPECIFIED: LongNoteAmount
LONG_NOTE_AMOUNT_TAP_ONLY: LongNoteAmount
LONG_NOTE_AMOUNT_HALF: LongNoteAmount
LONG_NOTE_AMOUNT_NATURAL: LongNoteAmount
PATTERN_KIND_UNSPECIFIED: PatternKind
PATTERN_KIND_STREAM: PatternKind
PATTERN_KIND_JUMPSTREAM: PatternKind
PATTERN_KIND_CHORDSTREAM: PatternKind
PATTERN_KIND_JACK: PatternKind
PATTERN_KIND_CHORDJACK: PatternKind
CONTROL_STATUS_UNSPECIFIED: ControlStatus
CONTROL_STATUS_WORKS: ControlStatus
CONTROL_STATUS_EXPERIMENTAL: ControlStatus
CONTROL_STATUS_NOT_WORKING: ControlStatus
GENERATION_PHASE_UNSPECIFIED: GenerationPhase
GENERATION_PHASE_LOADING: GenerationPhase
GENERATION_PHASE_TIMING: GenerationPhase
GENERATION_PHASE_ROWS: GenerationPhase
GENERATION_PHASE_ARRANGEMENT: GenerationPhase
GENERATION_PHASE_EXPORT: GenerationPhase

class ChartObject(_message.Message):
    __slots__ = ("lane", "start_ms", "end_ms")
    LANE_FIELD_NUMBER: _ClassVar[int]
    START_MS_FIELD_NUMBER: _ClassVar[int]
    END_MS_FIELD_NUMBER: _ClassVar[int]
    lane: int
    start_ms: int
    end_ms: int
    def __init__(self, lane: _Optional[int] = ..., start_ms: _Optional[int] = ..., end_ms: _Optional[int] = ...) -> None: ...

class Chart(_message.Message):
    __slots__ = ("duration_ms", "objects")
    DURATION_MS_FIELD_NUMBER: _ClassVar[int]
    OBJECTS_FIELD_NUMBER: _ClassVar[int]
    duration_ms: int
    objects: _containers.RepeatedCompositeFieldContainer[ChartObject]
    def __init__(self, duration_ms: _Optional[int] = ..., objects: _Optional[_Iterable[_Union[ChartObject, _Mapping]]] = ...) -> None: ...

class GenerateChartRequest(_message.Message):
    __slots__ = ("audio", "star", "seed", "controls", "title", "artist")
    AUDIO_FIELD_NUMBER: _ClassVar[int]
    STAR_FIELD_NUMBER: _ClassVar[int]
    SEED_FIELD_NUMBER: _ClassVar[int]
    CONTROLS_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    ARTIST_FIELD_NUMBER: _ClassVar[int]
    audio: _inference_pb2.AudioAssetRef
    star: float
    seed: int
    controls: ChartControls
    title: str
    artist: str
    def __init__(self, audio: _Optional[_Union[_inference_pb2.AudioAssetRef, _Mapping]] = ..., star: _Optional[float] = ..., seed: _Optional[int] = ..., controls: _Optional[_Union[ChartControls, _Mapping]] = ..., title: _Optional[str] = ..., artist: _Optional[str] = ...) -> None: ...

class ChartControls(_message.Message):
    __slots__ = ("long_notes", "sections")
    LONG_NOTES_FIELD_NUMBER: _ClassVar[int]
    SECTIONS_FIELD_NUMBER: _ClassVar[int]
    long_notes: LongNoteAmount
    sections: _containers.RepeatedCompositeFieldContainer[SectionRequest]
    def __init__(self, long_notes: _Optional[_Union[LongNoteAmount, str]] = ..., sections: _Optional[_Iterable[_Union[SectionRequest, _Mapping]]] = ...) -> None: ...

class SectionRequest(_message.Message):
    __slots__ = ("start_ms", "end_ms", "star", "pattern")
    START_MS_FIELD_NUMBER: _ClassVar[int]
    END_MS_FIELD_NUMBER: _ClassVar[int]
    STAR_FIELD_NUMBER: _ClassVar[int]
    PATTERN_FIELD_NUMBER: _ClassVar[int]
    start_ms: int
    end_ms: int
    star: float
    pattern: PatternRequest
    def __init__(self, start_ms: _Optional[int] = ..., end_ms: _Optional[int] = ..., star: _Optional[float] = ..., pattern: _Optional[_Union[PatternRequest, _Mapping]] = ...) -> None: ...

class PatternRequest(_message.Message):
    __slots__ = ("kind", "strength")
    KIND_FIELD_NUMBER: _ClassVar[int]
    STRENGTH_FIELD_NUMBER: _ClassVar[int]
    kind: PatternKind
    strength: float
    def __init__(self, kind: _Optional[_Union[PatternKind, str]] = ..., strength: _Optional[float] = ...) -> None: ...

class CapabilitiesRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ModelCapabilities(_message.Message):
    __slots__ = ("model_name", "model_version", "files", "min_star", "max_star_exclusive", "controls")
    MODEL_NAME_FIELD_NUMBER: _ClassVar[int]
    MODEL_VERSION_FIELD_NUMBER: _ClassVar[int]
    FILES_FIELD_NUMBER: _ClassVar[int]
    MIN_STAR_FIELD_NUMBER: _ClassVar[int]
    MAX_STAR_EXCLUSIVE_FIELD_NUMBER: _ClassVar[int]
    CONTROLS_FIELD_NUMBER: _ClassVar[int]
    model_name: str
    model_version: str
    files: _containers.RepeatedCompositeFieldContainer[ModelFile]
    min_star: float
    max_star_exclusive: float
    controls: _containers.RepeatedCompositeFieldContainer[ControlCapability]
    def __init__(self, model_name: _Optional[str] = ..., model_version: _Optional[str] = ..., files: _Optional[_Iterable[_Union[ModelFile, _Mapping]]] = ..., min_star: _Optional[float] = ..., max_star_exclusive: _Optional[float] = ..., controls: _Optional[_Iterable[_Union[ControlCapability, _Mapping]]] = ...) -> None: ...

class ModelFile(_message.Message):
    __slots__ = ("path", "sha256_hex")
    PATH_FIELD_NUMBER: _ClassVar[int]
    SHA256_HEX_FIELD_NUMBER: _ClassVar[int]
    path: str
    sha256_hex: str
    def __init__(self, path: _Optional[str] = ..., sha256_hex: _Optional[str] = ...) -> None: ...

class ControlCapability(_message.Message):
    __slots__ = ("name", "status", "note")
    NAME_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    NOTE_FIELD_NUMBER: _ClassVar[int]
    name: str
    status: ControlStatus
    note: str
    def __init__(self, name: _Optional[str] = ..., status: _Optional[_Union[ControlStatus, str]] = ..., note: _Optional[str] = ...) -> None: ...

class GenerationProgress(_message.Message):
    __slots__ = ("phase",)
    PHASE_FIELD_NUMBER: _ClassVar[int]
    phase: GenerationPhase
    def __init__(self, phase: _Optional[_Union[GenerationPhase, str]] = ...) -> None: ...

class ChartResult(_message.Message):
    __slots__ = ("chart", "receipt")
    CHART_FIELD_NUMBER: _ClassVar[int]
    RECEIPT_FIELD_NUMBER: _ClassVar[int]
    chart: Chart
    receipt: GenerationReceipt
    def __init__(self, chart: _Optional[_Union[Chart, _Mapping]] = ..., receipt: _Optional[_Union[GenerationReceipt, _Mapping]] = ...) -> None: ...

class GenerationReceipt(_message.Message):
    __slots__ = ("model_name", "model_version", "seed", "star", "receipt_json", "osz_path")
    MODEL_NAME_FIELD_NUMBER: _ClassVar[int]
    MODEL_VERSION_FIELD_NUMBER: _ClassVar[int]
    SEED_FIELD_NUMBER: _ClassVar[int]
    STAR_FIELD_NUMBER: _ClassVar[int]
    RECEIPT_JSON_FIELD_NUMBER: _ClassVar[int]
    OSZ_PATH_FIELD_NUMBER: _ClassVar[int]
    model_name: str
    model_version: str
    seed: int
    star: float
    receipt_json: str
    osz_path: str
    def __init__(self, model_name: _Optional[str] = ..., model_version: _Optional[str] = ..., seed: _Optional[int] = ..., star: _Optional[float] = ..., receipt_json: _Optional[str] = ..., osz_path: _Optional[str] = ...) -> None: ...

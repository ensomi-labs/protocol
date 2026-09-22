from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SyncSource(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SYNC_SOURCE_UNSPECIFIED: _ClassVar[SyncSource]
    SYNC_SOURCE_BACKGROUND: _ClassVar[SyncSource]
    SYNC_SOURCE_SYSTEM_AUDIO: _ClassVar[SyncSource]

class InferenceRoute(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    INFERENCE_ROUTE_UNSPECIFIED: _ClassVar[InferenceRoute]
    INFERENCE_ROUTE_MAPPER: _ClassVar[InferenceRoute]
    INFERENCE_ROUTE_TIMING_MOCK: _ClassVar[InferenceRoute]

class EndpointStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ENDPOINT_STATUS_UNSPECIFIED: _ClassVar[EndpointStatus]
    ENDPOINT_STATUS_READY: _ClassVar[EndpointStatus]
    ENDPOINT_STATUS_AUDIO_PREPARING: _ClassVar[EndpointStatus]
    ENDPOINT_STATUS_AUDIO_READY: _ClassVar[EndpointStatus]
    ENDPOINT_STATUS_STREAMING: _ClassVar[EndpointStatus]
    ENDPOINT_STATUS_STOPPED: _ClassVar[EndpointStatus]
    ENDPOINT_STATUS_FAILED: _ClassVar[EndpointStatus]
    ENDPOINT_STATUS_COLD: _ClassVar[EndpointStatus]
    ENDPOINT_STATUS_NO_SESSION: _ClassVar[EndpointStatus]

class InferenceErrorCode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    INFERENCE_ERROR_CODE_UNSPECIFIED: _ClassVar[InferenceErrorCode]
    INFERENCE_ERROR_CODE_PROTOCOL_ERROR: _ClassVar[InferenceErrorCode]
    INFERENCE_ERROR_CODE_INVALID_DEVICE: _ClassVar[InferenceErrorCode]
    INFERENCE_ERROR_CODE_AUDIO_NOT_FOUND: _ClassVar[InferenceErrorCode]
    INFERENCE_ERROR_CODE_INFERENCE_FAILED: _ClassVar[InferenceErrorCode]
    INFERENCE_ERROR_CODE_SESSION_NOT_FOUND: _ClassVar[InferenceErrorCode]
    INFERENCE_ERROR_CODE_SESSION_OWNERSHIP_CONFLICT: _ClassVar[InferenceErrorCode]
    INFERENCE_ERROR_CODE_AUDIO_NOT_PREPARED: _ClassVar[InferenceErrorCode]
    INFERENCE_ERROR_CODE_UNSUPPORTED_ROUTE: _ClassVar[InferenceErrorCode]
SYNC_SOURCE_UNSPECIFIED: SyncSource
SYNC_SOURCE_BACKGROUND: SyncSource
SYNC_SOURCE_SYSTEM_AUDIO: SyncSource
INFERENCE_ROUTE_UNSPECIFIED: InferenceRoute
INFERENCE_ROUTE_MAPPER: InferenceRoute
INFERENCE_ROUTE_TIMING_MOCK: InferenceRoute
ENDPOINT_STATUS_UNSPECIFIED: EndpointStatus
ENDPOINT_STATUS_READY: EndpointStatus
ENDPOINT_STATUS_AUDIO_PREPARING: EndpointStatus
ENDPOINT_STATUS_AUDIO_READY: EndpointStatus
ENDPOINT_STATUS_STREAMING: EndpointStatus
ENDPOINT_STATUS_STOPPED: EndpointStatus
ENDPOINT_STATUS_FAILED: EndpointStatus
ENDPOINT_STATUS_COLD: EndpointStatus
ENDPOINT_STATUS_NO_SESSION: EndpointStatus
INFERENCE_ERROR_CODE_UNSPECIFIED: InferenceErrorCode
INFERENCE_ERROR_CODE_PROTOCOL_ERROR: InferenceErrorCode
INFERENCE_ERROR_CODE_INVALID_DEVICE: InferenceErrorCode
INFERENCE_ERROR_CODE_AUDIO_NOT_FOUND: InferenceErrorCode
INFERENCE_ERROR_CODE_INFERENCE_FAILED: InferenceErrorCode
INFERENCE_ERROR_CODE_SESSION_NOT_FOUND: InferenceErrorCode
INFERENCE_ERROR_CODE_SESSION_OWNERSHIP_CONFLICT: InferenceErrorCode
INFERENCE_ERROR_CODE_AUDIO_NOT_PREPARED: InferenceErrorCode
INFERENCE_ERROR_CODE_UNSUPPORTED_ROUTE: InferenceErrorCode

class ReadyRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AudioAssetRef(_message.Message):
    __slots__ = ("local_path", "uri", "asset_id", "audio_length_ms", "sha256_hex")
    LOCAL_PATH_FIELD_NUMBER: _ClassVar[int]
    URI_FIELD_NUMBER: _ClassVar[int]
    ASSET_ID_FIELD_NUMBER: _ClassVar[int]
    AUDIO_LENGTH_MS_FIELD_NUMBER: _ClassVar[int]
    SHA256_HEX_FIELD_NUMBER: _ClassVar[int]
    local_path: str
    uri: str
    asset_id: str
    audio_length_ms: int
    sha256_hex: str
    def __init__(self, local_path: _Optional[str] = ..., uri: _Optional[str] = ..., asset_id: _Optional[str] = ..., audio_length_ms: _Optional[int] = ..., sha256_hex: _Optional[str] = ...) -> None: ...

class AudioRequest(_message.Message):
    __slots__ = ("audio", "sync_source", "difficulty", "route")
    AUDIO_FIELD_NUMBER: _ClassVar[int]
    SYNC_SOURCE_FIELD_NUMBER: _ClassVar[int]
    DIFFICULTY_FIELD_NUMBER: _ClassVar[int]
    ROUTE_FIELD_NUMBER: _ClassVar[int]
    audio: AudioAssetRef
    sync_source: SyncSource
    difficulty: float
    route: InferenceRoute
    def __init__(self, audio: _Optional[_Union[AudioAssetRef, _Mapping]] = ..., sync_source: _Optional[_Union[SyncSource, str]] = ..., difficulty: _Optional[float] = ..., route: _Optional[_Union[InferenceRoute, str]] = ...) -> None: ...

class ReferenceTimeRequest(_message.Message):
    __slots__ = ("ref_time_ms", "local_host_time_send_ms", "audio_length_ms")
    REF_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    LOCAL_HOST_TIME_SEND_MS_FIELD_NUMBER: _ClassVar[int]
    AUDIO_LENGTH_MS_FIELD_NUMBER: _ClassVar[int]
    ref_time_ms: int
    local_host_time_send_ms: int
    audio_length_ms: int
    def __init__(self, ref_time_ms: _Optional[int] = ..., local_host_time_send_ms: _Optional[int] = ..., audio_length_ms: _Optional[int] = ...) -> None: ...

class StopSessionRequest(_message.Message):
    __slots__ = ("reason",)
    REASON_FIELD_NUMBER: _ClassVar[int]
    reason: str
    def __init__(self, reason: _Optional[str] = ...) -> None: ...

class ErrorEvent(_message.Message):
    __slots__ = ("code", "message", "error_code", "phase", "route", "error_kind")
    CODE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ERROR_CODE_FIELD_NUMBER: _ClassVar[int]
    PHASE_FIELD_NUMBER: _ClassVar[int]
    ROUTE_FIELD_NUMBER: _ClassVar[int]
    ERROR_KIND_FIELD_NUMBER: _ClassVar[int]
    code: str
    message: str
    error_code: InferenceErrorCode
    phase: str
    route: InferenceRoute
    error_kind: str
    def __init__(self, code: _Optional[str] = ..., message: _Optional[str] = ..., error_code: _Optional[_Union[InferenceErrorCode, str]] = ..., phase: _Optional[str] = ..., route: _Optional[_Union[InferenceRoute, str]] = ..., error_kind: _Optional[str] = ...) -> None: ...

class StatusEvent(_message.Message):
    __slots__ = ("status", "message", "ref_time_ms", "sender_monotonic_ms", "from_status", "reason", "audio_length_ms", "reset_sender_monotonic_ms", "route", "difficulty")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    REF_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    SENDER_MONOTONIC_MS_FIELD_NUMBER: _ClassVar[int]
    FROM_STATUS_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    AUDIO_LENGTH_MS_FIELD_NUMBER: _ClassVar[int]
    RESET_SENDER_MONOTONIC_MS_FIELD_NUMBER: _ClassVar[int]
    ROUTE_FIELD_NUMBER: _ClassVar[int]
    DIFFICULTY_FIELD_NUMBER: _ClassVar[int]
    status: EndpointStatus
    message: str
    ref_time_ms: int
    sender_monotonic_ms: int
    from_status: EndpointStatus
    reason: str
    audio_length_ms: int
    reset_sender_monotonic_ms: int
    route: InferenceRoute
    difficulty: float
    def __init__(self, status: _Optional[_Union[EndpointStatus, str]] = ..., message: _Optional[str] = ..., ref_time_ms: _Optional[int] = ..., sender_monotonic_ms: _Optional[int] = ..., from_status: _Optional[_Union[EndpointStatus, str]] = ..., reason: _Optional[str] = ..., audio_length_ms: _Optional[int] = ..., reset_sender_monotonic_ms: _Optional[int] = ..., route: _Optional[_Union[InferenceRoute, str]] = ..., difficulty: _Optional[float] = ...) -> None: ...

class EndOfStreamEvent(_message.Message):
    __slots__ = ("audio_length_ms", "complete_through_ms")
    AUDIO_LENGTH_MS_FIELD_NUMBER: _ClassVar[int]
    COMPLETE_THROUGH_MS_FIELD_NUMBER: _ClassVar[int]
    audio_length_ms: int
    complete_through_ms: int
    def __init__(self, audio_length_ms: _Optional[int] = ..., complete_through_ms: _Optional[int] = ...) -> None: ...

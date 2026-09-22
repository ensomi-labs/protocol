from ensomi.protocol.v1 import core_pb2 as _core_pb2
from ensomi.protocol.v1 import inference_pb2 as _inference_pb2
from ensomi.protocol.v1 import mapper_pb2 as _mapper_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Envelope(_message.Message):
    __slots__ = ("session_id", "sequence", "sent_at_unix_ms", "source_node_id", "target_node_id", "message_id", "correlation_id", "node_hello", "ready", "audio", "reference_time", "stop_session", "mapper_stream_begin", "hit_object_token", "error", "status", "end_of_stream")
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    SEQUENCE_FIELD_NUMBER: _ClassVar[int]
    SENT_AT_UNIX_MS_FIELD_NUMBER: _ClassVar[int]
    SOURCE_NODE_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_NODE_ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    CORRELATION_ID_FIELD_NUMBER: _ClassVar[int]
    NODE_HELLO_FIELD_NUMBER: _ClassVar[int]
    READY_FIELD_NUMBER: _ClassVar[int]
    AUDIO_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_TIME_FIELD_NUMBER: _ClassVar[int]
    STOP_SESSION_FIELD_NUMBER: _ClassVar[int]
    MAPPER_STREAM_BEGIN_FIELD_NUMBER: _ClassVar[int]
    HIT_OBJECT_TOKEN_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    END_OF_STREAM_FIELD_NUMBER: _ClassVar[int]
    session_id: str
    sequence: int
    sent_at_unix_ms: int
    source_node_id: str
    target_node_id: str
    message_id: str
    correlation_id: str
    node_hello: _core_pb2.NodeHello
    ready: _inference_pb2.ReadyRequest
    audio: _inference_pb2.AudioRequest
    reference_time: _inference_pb2.ReferenceTimeRequest
    stop_session: _inference_pb2.StopSessionRequest
    mapper_stream_begin: _mapper_pb2.MapperStreamBeginEvent
    hit_object_token: _mapper_pb2.HitObjectTokenEvent
    error: _inference_pb2.ErrorEvent
    status: _inference_pb2.StatusEvent
    end_of_stream: _inference_pb2.EndOfStreamEvent
    def __init__(self, session_id: _Optional[str] = ..., sequence: _Optional[int] = ..., sent_at_unix_ms: _Optional[int] = ..., source_node_id: _Optional[str] = ..., target_node_id: _Optional[str] = ..., message_id: _Optional[str] = ..., correlation_id: _Optional[str] = ..., node_hello: _Optional[_Union[_core_pb2.NodeHello, _Mapping]] = ..., ready: _Optional[_Union[_inference_pb2.ReadyRequest, _Mapping]] = ..., audio: _Optional[_Union[_inference_pb2.AudioRequest, _Mapping]] = ..., reference_time: _Optional[_Union[_inference_pb2.ReferenceTimeRequest, _Mapping]] = ..., stop_session: _Optional[_Union[_inference_pb2.StopSessionRequest, _Mapping]] = ..., mapper_stream_begin: _Optional[_Union[_mapper_pb2.MapperStreamBeginEvent, _Mapping]] = ..., hit_object_token: _Optional[_Union[_mapper_pb2.HitObjectTokenEvent, _Mapping]] = ..., error: _Optional[_Union[_inference_pb2.ErrorEvent, _Mapping]] = ..., status: _Optional[_Union[_inference_pb2.StatusEvent, _Mapping]] = ..., end_of_stream: _Optional[_Union[_inference_pb2.EndOfStreamEvent, _Mapping]] = ...) -> None: ...

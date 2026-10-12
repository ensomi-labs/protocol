from ensomi.protocol.v1 import chart_pb2 as _chart_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ChartStreamRequest(_message.Message):
    __slots__ = ("generation",)
    GENERATION_FIELD_NUMBER: _ClassVar[int]
    generation: _chart_pb2.GenerateChartRequest
    def __init__(self, generation: _Optional[_Union[_chart_pb2.GenerateChartRequest, _Mapping]] = ...) -> None: ...

class ChartStreamOpened(_message.Message):
    __slots__ = ("duration_ms",)
    DURATION_MS_FIELD_NUMBER: _ClassVar[int]
    duration_ms: int
    def __init__(self, duration_ms: _Optional[int] = ...) -> None: ...

class ChartPageRequest(_message.Message):
    __slots__ = ("after_sequence", "through_ms")
    AFTER_SEQUENCE_FIELD_NUMBER: _ClassVar[int]
    THROUGH_MS_FIELD_NUMBER: _ClassVar[int]
    after_sequence: int
    through_ms: int
    def __init__(self, after_sequence: _Optional[int] = ..., through_ms: _Optional[int] = ...) -> None: ...

class ChartPage(_message.Message):
    __slots__ = ("sequence", "coverage_ms", "end_of_stream", "objects", "receipt")
    SEQUENCE_FIELD_NUMBER: _ClassVar[int]
    COVERAGE_MS_FIELD_NUMBER: _ClassVar[int]
    END_OF_STREAM_FIELD_NUMBER: _ClassVar[int]
    OBJECTS_FIELD_NUMBER: _ClassVar[int]
    RECEIPT_FIELD_NUMBER: _ClassVar[int]
    sequence: int
    coverage_ms: int
    end_of_stream: bool
    objects: _containers.RepeatedCompositeFieldContainer[_chart_pb2.ChartObject]
    receipt: _chart_pb2.GenerationReceipt
    def __init__(self, sequence: _Optional[int] = ..., coverage_ms: _Optional[int] = ..., end_of_stream: bool = ..., objects: _Optional[_Iterable[_Union[_chart_pb2.ChartObject, _Mapping]]] = ..., receipt: _Optional[_Union[_chart_pb2.GenerationReceipt, _Mapping]] = ...) -> None: ...

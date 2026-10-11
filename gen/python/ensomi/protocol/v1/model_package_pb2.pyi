from ensomi.protocol.v1 import chart_pb2 as _chart_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ModelGraph(_message.Message):
    __slots__ = ("name", "file", "opset")
    NAME_FIELD_NUMBER: _ClassVar[int]
    FILE_FIELD_NUMBER: _ClassVar[int]
    OPSET_FIELD_NUMBER: _ClassVar[int]
    name: str
    file: str
    opset: int
    def __init__(self, name: _Optional[str] = ..., file: _Optional[str] = ..., opset: _Optional[int] = ...) -> None: ...

class RuntimeVersionRange(_message.Message):
    __slots__ = ("min_version", "max_version_exclusive")
    MIN_VERSION_FIELD_NUMBER: _ClassVar[int]
    MAX_VERSION_EXCLUSIVE_FIELD_NUMBER: _ClassVar[int]
    min_version: str
    max_version_exclusive: str
    def __init__(self, min_version: _Optional[str] = ..., max_version_exclusive: _Optional[str] = ...) -> None: ...

class ModelPackageManifest(_message.Message):
    __slots__ = ("model_name", "model_version", "license", "files", "graphs", "runtime_config_path", "runtime_versions")
    MODEL_NAME_FIELD_NUMBER: _ClassVar[int]
    MODEL_VERSION_FIELD_NUMBER: _ClassVar[int]
    LICENSE_FIELD_NUMBER: _ClassVar[int]
    FILES_FIELD_NUMBER: _ClassVar[int]
    GRAPHS_FIELD_NUMBER: _ClassVar[int]
    RUNTIME_CONFIG_PATH_FIELD_NUMBER: _ClassVar[int]
    RUNTIME_VERSIONS_FIELD_NUMBER: _ClassVar[int]
    model_name: str
    model_version: str
    license: str
    files: _containers.RepeatedCompositeFieldContainer[_chart_pb2.ModelFile]
    graphs: _containers.RepeatedCompositeFieldContainer[ModelGraph]
    runtime_config_path: str
    runtime_versions: RuntimeVersionRange
    def __init__(self, model_name: _Optional[str] = ..., model_version: _Optional[str] = ..., license: _Optional[str] = ..., files: _Optional[_Iterable[_Union[_chart_pb2.ModelFile, _Mapping]]] = ..., graphs: _Optional[_Iterable[_Union[ModelGraph, _Mapping]]] = ..., runtime_config_path: _Optional[str] = ..., runtime_versions: _Optional[_Union[RuntimeVersionRange, _Mapping]] = ...) -> None: ...

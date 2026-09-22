from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NodeRole(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NODE_ROLE_UNSPECIFIED: _ClassVar[NodeRole]
    NODE_ROLE_HOST: _ClassVar[NodeRole]
    NODE_ROLE_PLAYER_CLIENT: _ClassVar[NodeRole]
    NODE_ROLE_MODEL_SERVICE: _ClassVar[NodeRole]
    NODE_ROLE_HARDWARE: _ClassVar[NodeRole]
    NODE_ROLE_DEBUG_TOOL: _ClassVar[NodeRole]

class NodeCapabilityKind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NODE_CAPABILITY_KIND_UNSPECIFIED: _ClassVar[NodeCapabilityKind]
    NODE_CAPABILITY_KIND_RECOGNITION: _ClassVar[NodeCapabilityKind]
    NODE_CAPABILITY_KIND_TIMING: _ClassVar[NodeCapabilityKind]
    NODE_CAPABILITY_KIND_MAPPER: _ClassVar[NodeCapabilityKind]
    NODE_CAPABILITY_KIND_PLAYER_STREAM: _ClassVar[NodeCapabilityKind]
    NODE_CAPABILITY_KIND_HARDWARE: _ClassVar[NodeCapabilityKind]
    NODE_CAPABILITY_KIND_DEBUG: _ClassVar[NodeCapabilityKind]

class NodeCapabilityDirection(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NODE_CAPABILITY_DIRECTION_UNSPECIFIED: _ClassVar[NodeCapabilityDirection]
    NODE_CAPABILITY_DIRECTION_PRODUCER: _ClassVar[NodeCapabilityDirection]
    NODE_CAPABILITY_DIRECTION_CONSUMER: _ClassVar[NodeCapabilityDirection]
    NODE_CAPABILITY_DIRECTION_BIDIRECTIONAL: _ClassVar[NodeCapabilityDirection]
NODE_ROLE_UNSPECIFIED: NodeRole
NODE_ROLE_HOST: NodeRole
NODE_ROLE_PLAYER_CLIENT: NodeRole
NODE_ROLE_MODEL_SERVICE: NodeRole
NODE_ROLE_HARDWARE: NodeRole
NODE_ROLE_DEBUG_TOOL: NodeRole
NODE_CAPABILITY_KIND_UNSPECIFIED: NodeCapabilityKind
NODE_CAPABILITY_KIND_RECOGNITION: NodeCapabilityKind
NODE_CAPABILITY_KIND_TIMING: NodeCapabilityKind
NODE_CAPABILITY_KIND_MAPPER: NodeCapabilityKind
NODE_CAPABILITY_KIND_PLAYER_STREAM: NodeCapabilityKind
NODE_CAPABILITY_KIND_HARDWARE: NodeCapabilityKind
NODE_CAPABILITY_KIND_DEBUG: NodeCapabilityKind
NODE_CAPABILITY_DIRECTION_UNSPECIFIED: NodeCapabilityDirection
NODE_CAPABILITY_DIRECTION_PRODUCER: NodeCapabilityDirection
NODE_CAPABILITY_DIRECTION_CONSUMER: NodeCapabilityDirection
NODE_CAPABILITY_DIRECTION_BIDIRECTIONAL: NodeCapabilityDirection

class NodeCapability(_message.Message):
    __slots__ = ("kind", "name", "version", "direction")
    KIND_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    DIRECTION_FIELD_NUMBER: _ClassVar[int]
    kind: NodeCapabilityKind
    name: str
    version: str
    direction: NodeCapabilityDirection
    def __init__(self, kind: _Optional[_Union[NodeCapabilityKind, str]] = ..., name: _Optional[str] = ..., version: _Optional[str] = ..., direction: _Optional[_Union[NodeCapabilityDirection, str]] = ...) -> None: ...

class NodeHello(_message.Message):
    __slots__ = ("node_id", "role", "capabilities", "protocol_version", "app_id")
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    PROTOCOL_VERSION_FIELD_NUMBER: _ClassVar[int]
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    node_id: str
    role: NodeRole
    capabilities: _containers.RepeatedCompositeFieldContainer[NodeCapability]
    protocol_version: str
    app_id: str
    def __init__(self, node_id: _Optional[str] = ..., role: _Optional[_Union[NodeRole, str]] = ..., capabilities: _Optional[_Iterable[_Union[NodeCapability, _Mapping]]] = ..., protocol_version: _Optional[str] = ..., app_id: _Optional[str] = ...) -> None: ...

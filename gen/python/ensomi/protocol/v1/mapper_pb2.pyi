from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class MapperStreamBeginEvent(_message.Message):
    __slots__ = ("token_contract_version", "audio_length_ms")
    TOKEN_CONTRACT_VERSION_FIELD_NUMBER: _ClassVar[int]
    AUDIO_LENGTH_MS_FIELD_NUMBER: _ClassVar[int]
    token_contract_version: int
    audio_length_ms: int
    def __init__(self, token_contract_version: _Optional[int] = ..., audio_length_ms: _Optional[int] = ...) -> None: ...

class HitObjectTokenEvent(_message.Message):
    __slots__ = ("token_id", "ms_in_ref_audio", "token_index")
    TOKEN_ID_FIELD_NUMBER: _ClassVar[int]
    MS_IN_REF_AUDIO_FIELD_NUMBER: _ClassVar[int]
    TOKEN_INDEX_FIELD_NUMBER: _ClassVar[int]
    token_id: int
    ms_in_ref_audio: int
    token_index: int
    def __init__(self, token_id: _Optional[int] = ..., ms_in_ref_audio: _Optional[int] = ..., token_index: _Optional[int] = ...) -> None: ...

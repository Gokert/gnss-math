from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Coordinate(_message.Message):
    __slots__ = ("x", "y", "z")
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    Z_FIELD_NUMBER: _ClassVar[int]
    x: float
    y: float
    z: float
    def __init__(self, x: _Optional[float] = ..., y: _Optional[float] = ..., z: _Optional[float] = ...) -> None: ...

class ListCoordinatesRequest(_message.Message):
    __slots__ = ("satellite_name",)
    SATELLITE_NAME_FIELD_NUMBER: _ClassVar[int]
    satellite_name: str
    def __init__(self, satellite_name: _Optional[str] = ...) -> None: ...

class ListCoordinatesResponse(_message.Message):
    __slots__ = ("coordinates",)
    COORDINATES_FIELD_NUMBER: _ClassVar[int]
    coordinates: _containers.RepeatedCompositeFieldContainer[Coordinate]
    def __init__(self, coordinates: _Optional[_Iterable[_Union[Coordinate, _Mapping]]] = ...) -> None: ...

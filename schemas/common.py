import typing

from pydantic import BaseModel
from pydantic.generics import GenericModel

ModelType = typing.TypeVar("ModelType")


class Page(GenericModel, typing.Generic[ModelType]):
    total: int = None
    record: typing.Optional[ModelType] | None = None


class BatchDto(BaseModel):
    data: list[int] = None

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True

import typing
from typing import List
from datetime import datetime

from pydantic import BaseModel
from pydantic.generics import GenericModel

ModelType = typing.TypeVar("ModelType")


class Common(BaseModel):
    create_time: datetime = None
    update_time: datetime = None

    class Config:
        orm_mode = True


class Page(GenericModel, typing.Generic[ModelType]):
    total: int
    record: typing.Optional[ModelType] | None = None


class BatchDto(BaseModel):
    data: List[int] = None

    class Config:
        orm_mode = True

# coding: utf-8

from __future__ import annotations

from typing import Optional

# from odmantic import Field , Model
from pydantic import Field, BaseModel as Model


class Person(Model):
    name: Optional[str] = Field(None)
    rooms: "Optional[Room]" = Field(None)


from ..models.room import Room  # nopep8
Person.update_forward_refs()

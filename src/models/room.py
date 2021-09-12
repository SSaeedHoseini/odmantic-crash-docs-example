# coding: utf-8

from __future__ import annotations

from typing import Optional



# from odmantic import Field, Model
from pydantic import Field, BaseModel as Model


class Room(Model):
    name: Optional[str] = Field(None)
    persons: Optional[Person] = Field(None)


from ..models.person import Person  # nopep8
Room.update_forward_refs()

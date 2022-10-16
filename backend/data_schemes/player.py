from pydantic import BaseModel
from typing import Union
from statistics import Statistics


class Player(BaseModel):
    firstName: Union[str, None] = None
    lastName: Union[str, None] = None
    personId: Union[str, None] = None
    teamId: Union[str, None] = None
    jersey: Union[str, None] = None
    pos: Union[str, None] = None
    isActive: bool
    img: Union[str, None] = None

from pydantic import BaseModel
from typing import Union
from statistics import Statistics


class Player(BaseModel):
    playerId: Union[str, None] = None
    fName: Union[str, None] = None
    lName: Union[str, None] = None
    jersey: Union[str, None] = None
    positon: Union[str, None] = None
    img: Union[str, None] = None
    isActive: bool = False
    statistics: Union[Statistics, None] = None

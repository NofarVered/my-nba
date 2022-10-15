from pydantic import BaseModel
from typing import Union


class Statistics(BaseModel):
    rating: Union[str, None] = None
    minutes_per_game: Union[str, None] = None
    field_shots: Union[str, None] = None
    free_shots: Union[str, None] = None
    three_point_shots: Union[str, None] = None

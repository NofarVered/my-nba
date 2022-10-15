from pydantic import BaseModel
from typing import Union


class Statistics(BaseModel):
    minutes_per_game: Union[str, None] = None
    field_goal_percentage: Union[str, None] = None
    free_throw_percentage: Union[str, None] = None
    three_point_percentage: Union[str, None] = None
    player_efficiency_rating: Union[str, None] = None

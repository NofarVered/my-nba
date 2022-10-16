from pydantic import BaseModel
from typing import Union


class Statistics(BaseModel):
    games_played: Union[str, None] = None
    minutes_per_game: Union[str, None] = None
    free_throw_percentage: Union[str, None] = None
    player_efficiency_rating: Union[str, None] = None

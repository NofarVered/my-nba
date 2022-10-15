from pydantic import BaseModel
from typing import *

from player import Player


class DreamTeam():
    def __init__(self):
        self.players = Union[list[Player], None] = None

    def remove_player(self, player_id: str):
        return {"message": "player {player_id} removed from the team!"}

    def add_player(self, player_id: str):
        return {"message": "player {player_id} added to the team!"}

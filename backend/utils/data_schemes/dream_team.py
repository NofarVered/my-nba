import json
from pydantic import BaseModel
from typing import *

from player import Player


class DreamTeam():
    def __init__(self):
        self.team = Union[list[Player], None] = None

    def get_dream_team(self):
        return self.team

    def remove_player(self, personId: str):
        self.team = list(
            filter(lambda player: player.personId != personId, self.team))
        return {"message": "player removed from the team!"}

# TO DO!
    def add_player(self, player: json):
        self.team.append(Player(player))
        return {"message": "player added to the team!"}

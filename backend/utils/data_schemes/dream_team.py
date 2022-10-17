import json
from pydantic import BaseModel
from typing import *

from player import Player


class DreamTeam():
    def __init__(self):
        self.team = []

    def get_dream_team(self):
        return self.team

    def remove_player(self, personId: str):
        self.team = list(
            filter(lambda player: player.personId != personId, self.team))

    def add_player(self, player: Player):
        self.team.append(player)

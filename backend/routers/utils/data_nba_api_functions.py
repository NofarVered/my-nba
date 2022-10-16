from ...structures.teams_id import teams_id
from ...structures.player import Player
from .url import *


def filter_by_team(players_response, teamName, isActive):
    result = [Player(**curr_player, img=IMG_URL % (
        curr_player["lastName"], curr_player["firstName"])) for curr_player in players_response if curr_player["teamId"] == teams_id[teamName]]
    if (isActive):
        result = [Player(**curr_player, img=IMG_URL % (
            curr_player["lastName"], curr_player["firstName"])) for curr_player in players_response if curr_player["teamId"] == teams_id[teamName] and curr_player["isActive"] == True]
    return result


def filter_player_stats(stats_response):
    result = []

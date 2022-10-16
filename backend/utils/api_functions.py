from .data_schemes.teams_id import teams_id
from .data_schemes.player import Player
from .url import url_const


class ApiFunctions:

    @staticmethod
    def filter_by_team(players_response, teamName, isActive):
        print(isActive == False)
        result = [Player(**curr_player, img=url_const['IMG_URL'] % (
            curr_player["lastName"], curr_player["firstName"])) for curr_player in players_response if curr_player["teamId"] == teams_id[teamName]]
        if (isActive):
            result = [p for p in result if p.isActive]
        return result

    @staticmethod
    def filter_player_stats(stats_response):
        # TO DO
        result = []
        return result

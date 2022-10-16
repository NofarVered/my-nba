from fastapi import APIRouter, HTTPException, status
import requests
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import uvicorn
import requests
from .data_nba_api_functions import *
from .url import *

router = APIRouter()


@router.get("/players")
async def get_players(teamName: str = "", year: str = "", isActive: bool = False):
    try:
        players_response = requests.get(
            BY_YEAR_PLAYERS % (year)).json()["league"]["standard"]
        filtered_players = filter_by_team(
            players_response, teamName, isActive)
        return {"players": filtered_players}
    except requests.exceptions.HTTPError as err:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Invalid team"
        )


@router.get("/players/stats/{first_name}/{last_name}")
def get_player_stats(first_name: str = "", last_name: str = ""):
    try:
        stats_response = requests.get(PLAYER_STATS %
                                      (last_name, first_name)).json()
        player_stats = filter_player_stats(stats_response)
        return {"stats": player_stats}
    except requests.exceptions.HTTPError as err:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Invalid player name or last name"
        )

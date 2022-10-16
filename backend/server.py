from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import uvicorn
from fastapi import HTTPException, status
import requests
from utils.url import url_const
from utils.api_functions import ApiFunctions

app = FastAPI()

app.mount("/", StaticFiles(directory="../frontend", html=True), name="frontend")


@app.get("/")
def root():
    return {"message": "Server is up and running"}


@app.get("/players")
async def get_players(teamName: str = "", year: str = "", isActive: bool = False):
    try:
        players_response = requests.get(
            url_const['BY_YEAR_PLAYERS'] % (year)).json()["league"]["standard"]
        filtered_players = ApiFunctions.filter_by_team(
            players_response, teamName, isActive)
        return {"players": filtered_players}
    except requests.exceptions.HTTPError as err:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Invalid team"
        )


@app.get("/players/stats/{first_name}/{last_name}")
def get_player_stats(first_name: str = "", last_name: str = ""):
    try:
        stats_response = requests.get(url_const['PLAYER_STATS'] %
                                      (last_name, first_name)).json()
        player_stats = ApiFunctions.filter_player_stats(stats_response)
        return {"stats": player_stats}
    except requests.exceptions.HTTPError as err:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Invalid player name or last name"
        )


if __name__ == "__main__":
    uvicorn.run("server:app", host="0.0.0.0", port=8000, reload=True)

from fastapi import FastAPI, Request, Response
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import uvicorn
from fastapi import HTTPException, status
import requests
from utils.url import url_const
from utils.api_services import ApiFunctions
from utils.data_schemes.dream_team import DreamTeam
from utils.data_schemes.player import Player

dreamTeam = DreamTeam()

app = FastAPI()


@app.get("/sanity")
def root():
    return {"message": "Server is running"}


@app.get("/search")
async def get_players(teamName: str = "", year: str = "", isActive: bool = False):
    try:
        players_response = requests.get(
            url_const['BY_YEAR_PLAYERS'] % (year)).json()["league"]["standard"]
        filtered_players = ApiFunctions.filter_by_team(
            players_response, teamName, isActive)
        return {"team": filtered_players}
    except requests.exceptions.HTTPError as err:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Invalid team"
        )


@app.get("/stats")
def get_player_stats(firstName: str = "", lastName: str = ""):
    try:
        stats_response = requests.get(url_const['PLAYER_STATS'] %
                                      (lastName, firstName)).json()
        player_stats = ApiFunctions.filter_player_stats(
            stats_response)
        return {"stats": player_stats}
    except requests.exceptions.HTTPError as err:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Invalid player name or last name"
        )


@app.get("/dream")
def get_dream_team():
    return dreamTeam


@app.post("/dream")
async def add_to_dream_team(request: Request, response: Response):
    req = await request.json()
    player = Player(**req)
    dreamTeam.add_player(player)
    response.status_code = status.HTTP_201_CREATED
    return {"new team": dreamTeam.get_dream_team()}


@app.delete("/dream")
async def delete_dream_team(request: Request, response: Response):
    req = await request.json()
    dreamTeam.remove_player(
        req["personId"])
    response.status_code = status.HTTP_204_NO_CONTENT
    return {"new team": dreamTeam.get_dream_team()
            }


app.mount("/", StaticFiles(directory="../frontend", html=True), name="frontend")

if __name__ == "__main__":
    uvicorn.run("server:app", host="127.0.0.1", port=8000, reload=True)

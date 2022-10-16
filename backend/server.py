from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import uvicorn
from fastapi import HTTPException, status
import requests
from utils.url import url_const
from utils.api_functions import ApiFunctions

app = FastAPI()


@app.get("/sanity")
def root():
    return {"message": "Server is running"}


# localhost:8000/search?teamName=warriors&year=2018&isActive=true
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


# localhost:8000/stats?lastName=james&firstName=lebron
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


app.mount("/", StaticFiles(directory="../frontend", html=True), name="frontend")

if __name__ == "__main__":
    uvicorn.run("server:app", host="127.0.0.1", port=8000, reload=True)

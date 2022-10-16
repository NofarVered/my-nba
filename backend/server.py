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

# @app.get("/dreamTeam")
# def getDreamTeam():
#     return dreamTeam


# @app.post("/dreamTeam")
# async def add_player_to_dream_team(playerRequest: Request, response: Response) -> None:
#     player = await playerRequest.json()
#     if (player in dreamTeam.players):
#         raise HTTPException(
#             status_code=500, detail="Player already exisit in dream-team!")
#     player['isInDreamTeam'] = True
#     dreamTeam.add_player(player)
#     response.status_code = status.HTTP_201_CREATED
#     return player


# @app.delete("/dreamTeam")
# def delete_player_from_dream_team(playerId: str, response: Response) -> None:
#     playerToDelete = None
#     for player in dreamTeam.players:
#         if player.get('personId') == playerId:
#             playerToDelete = player
#             break
#     if playerToDelete is None:
#         raise HTTPException(
#             status_code=500, detail="Player not found in dream-team!")
#     indexToDelete = dreamTeam.players.index(player)
#     dreamTeam.players.pop(indexToDelete)
#     response.status_code = status.HTTP_204_NO_CONTENT
#     return

app.mount("/", StaticFiles(directory="../frontend", html=True), name="frontend")

if __name__ == "__main__":
    uvicorn.run("server:app", host="127.0.0.1", port=8000, reload=True)

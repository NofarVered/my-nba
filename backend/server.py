from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from routers import data_nba_api
import uvicorn

app = FastAPI()
app.include_router(data_nba_api.router)

app.mount("/frontend/build",
          StaticFiles(directory="frontend/build"), name="static")


@app.get("/")
def root():
    return FileResponse("./frontend/build/index.html")


if __name__ == "__main__":
    uvicorn.run("server:app", host="0.0.0.0", port=8000, reload=True)

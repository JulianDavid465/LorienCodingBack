from typing import Optional
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
import databaseApp

# Command to initialize server
# uvicorn main:app --reload

app = FastAPI()

"""
class GameIN(BaseModel):
    id: int
    name: str

class GameOUT(BaseModel):
    id: int
    name: str
    resultOperation : str


@app.post("/game/", response_model=GameOUT, status_code=status.HTTP_201_CREATED)
async def create_game(game : GameIN):
    databaseGame.addGame(game.name)
    return GameOUT(id = 0, name = game.name, resultOperation = "Game Created")

@app.get("/game/")
async def get_games_list():
    return databaseGame.getGames()
"""

@app.get("/")
async def readRoot():
    data = databaseApp.addData()
    return ("Hello World", data[0])
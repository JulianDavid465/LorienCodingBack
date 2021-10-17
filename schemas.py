from typing import Optional
from pydantic import BaseModel


class GameIN(BaseModel):
    name: str

    class Config:
        orm_mode = True


class GameInDB(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


class GameOUT(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True

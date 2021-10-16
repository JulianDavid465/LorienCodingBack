from typing import Optional
from pydantic import BaseModel


class GameIN(BaseModel):
    name: str

    class Config:
        orm_mode = True


class GameInDB(BaseModel):
    name: str

    class Config:
        orm_mode = True


class GameOUT(BaseModel):
    name: str
    operationResult: str

    class Config:
        orm_mode = True

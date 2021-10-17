from typing import Optional, Set, List
from pydantic import BaseModel, validator


class Player(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


class GameIN(BaseModel):
    name: str
    password: Optional[str]

    class Config:
        orm_mode = True


class GameInDB(BaseModel):
    id: int
    name: str
    password: Optional[str]
    state: int
    playersID: List[Player]

    @validator("playersID", pre=True, allow_reuse=True)
    def pony_set_to_list(cls, values):
        return [v.to_dict() for v in values]

    class Config:
        orm_mode = True


class GameOUT(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True

from pydantic import BaseModel


class GameIn(BaseModel):
    height: int = 50
    width: int = 50

from pydantic import BaseModel
from player import Player

def team_validation(team) -> None:
    pass

class Team(BaseModel):
    name : str
    players : list[Player]
    wins_needed : int

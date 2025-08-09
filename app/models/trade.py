from pydantic import BaseModel
from .player import Player

class trade(BaseModel):
    teamA : str
    teamB : str
    players_from_A : list[Player]
    players_from_B : list[Player]
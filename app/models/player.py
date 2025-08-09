from pydantic import BaseModel
from typing import Optional

class Player(BaseModel):
    id : int
    name : Optional[str]
    team : str
    games_played : float
    ppg : float
    rpg : float
    apg : float
    fppg : float
    games_remaining : int
    injured : bool

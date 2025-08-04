from pydantic import basemodel

class Player(basemodel):
    id : str
    name : str
    team : str
    games_played : float
    ppg : float
    rpg : float
    apg : float
    position : list[str]
    fppg : float
    games_remaining : int
    injury_status : str

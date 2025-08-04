from ..models.player import Player

def projections(player: Player) -> float:
    injury_multiplier = {
        "Healthy": 1.0,
        "DTD": 0.8,
        "Out": 0.2
    }.get(player.injury_status,1.0)

    return player.fppg * player.games_remaining * injury_multiplier
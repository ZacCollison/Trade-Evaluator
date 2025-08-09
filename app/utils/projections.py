from ..models.player import Player

def projections(player: Player) -> float:

    if player.injured:
        injury_multiplier = 0.2
    else:
        injury_multiplier = 1.0

    return player.fppg * player.games_remaining * injury_multiplier
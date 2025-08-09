'''
This file is used to evaluate the trade between 2 players and determine if it is fair based on projected points for rest of season.
In future iterations injuries will be considered and also positions required of a team.
'''

from ..models.player import Player
from ..models.trade import trade
from ..utils.projections import projections

def evaluate_trade(trade: trade):
    gain_a = sum(projections(p) for p in trade.players_from_b)
    loss_a = sum(projections(p) for p in trade.players_from_a)
    net_gain_a = gain_a - loss_a

    gain_b = sum(projections(p) for p in trade.players_from_a)
    loss_b = sum(projections(p) for p in trade.players_from_b)
    net_gain_b = gain_b - loss_b

    fairness_score = 100 - abs(net_gain_a - net_gain_b)  # 100 = perfectly fair

    winner = trade.team_a_name if net_gain_a > net_gain_b else trade.team_b_name

    return {
        "winner": winner,
        "net_gain_team_a": net_gain_a,
        "net_gain_team_b": net_gain_b,
        "fairness_score": round(fairness_score, 2)
    }
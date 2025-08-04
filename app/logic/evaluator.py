from ..models.player import Player
from ..models.trade import TradeProposal
from ..utils.projections import projected_points

def evaluate_trade(trade: TradeProposal):
    gain_a = sum(projected_points(p) for p in trade.players_from_b)
    loss_a = sum(projected_points(p) for p in trade.players_from_a)
    net_gain_a = gain_a - loss_a

    gain_b = sum(projected_points(p) for p in trade.players_from_a)
    loss_b = sum(projected_points(p) for p in trade.players_from_b)
    net_gain_b = gain_b - loss_b

    fairness_score = 100 - abs(net_gain_a - net_gain_b)  # Basic fairness metric (closer = fairer)

    winner = trade.team_a_name if net_gain_a > net_gain_b else trade.team_b_name

    return {
        "winner": winner,
        "net_gain_team_a": net_gain_a,
        "net_gain_team_b": net_gain_b,
        "fairness_score": round(fairness_score, 2)
    }
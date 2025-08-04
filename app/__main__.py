# from fastapi import FastAPI
# from app.models.trade import TradeProposal
# from app.logic.evaluator import evaluate_trade

# app = FastAPI()

# @app.post("/evaluate")
# def evaluate(trade: TradeProposal):
#     return evaluate_trade(trade)

from app.data.Process_player import get_all_players

if __name__ == "__main__":
    objs = get_all_players()
    for obj in objs[:5]:
        print(obj)
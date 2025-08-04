from fastapi import FastAPI
from app.models.trade import TradeProposal
from app.logic.evaluator import evaluate_trade

app = FastAPI()

@app.post("/evaluate")
def evaluate(trade: TradeProposal):
    return evaluate_trade(trade)

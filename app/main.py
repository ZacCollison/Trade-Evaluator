from fastapi import FastAPI
from app.models.trade import trade
from app.logic.evaluator import evaluate_trade

app = FastAPI(title="NBA Fantasy Trade Evaluator")

@app.get("/")
def root():
    return {"message": "FastAPI is running!"}

@app.post("/evaluate-trade")
def evaluate(trade: trade):
    result = evaluate_trade(trade)
    return {"evaluation": result}

# if __name__ == "__main__":
#     uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Example in-memory storage for funds and other data (you may replace this with a database)
account_balance = 1000.50
loan_balance = 0
credit_score = 750

class Transaction(BaseModel):
    amount: float
    to: str = None  # Optional, used for transfer actions

@app.get("/api/balance")
async def get_balance():
    # Returns the current account balance
    return {"balance": account_balance}

@app.post("/api/transfer")
async def transfer_funds(transaction: Transaction):
    global account_balance
    # Simulate transferring funds
    if account_balance >= transaction.amount:
        account_balance -= transaction.amount
        return {"status": "success", "message": f"Transferred ${transaction.amount} to {transaction.to}"}
    else:
        return {"status": "error", "message": "Insufficient funds for transfer"}

@app.post("/api/withdraw")
async def withdraw(transaction: Transaction):
    global account_balance
    # Simulate withdrawing funds
    if account_balance >= transaction.amount:
        account_balance -= transaction.amount
        return {"status": "success", "message": f"Withdrew ${transaction.amount}"}
    else:
        return {"status": "error", "message": "Insufficient funds for withdrawal"}

@app.post("/api/deposit")
async def deposit(transaction: Transaction):
    global account_balance
    # Simulate depositing funds
    account_balance += transaction.amount
    return {"status": "success", "message": f"Deposited ${transaction.amount}"}

@app.post("/api/loan")
async def apply_for_loan(transaction: Transaction):
    global loan_balance
    # Simulate applying for a loan
    loan_balance += transaction.amount
    return {"status": "success", "message": f"Loan of ${transaction.amount} approved"}

@app.get("/api/credit_score")
async def get_credit_score():
    # Returns the current credit score
    return {"credit_score": credit_score}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

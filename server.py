from fastapi import FastAPI, Request
from fastapi.routing import APIRoute
from pydantic import BaseModel

app = FastAPI()

# In-memory storage
account_balance = 0.00
loan_balance = 0
credit_score = 0

class Transaction(BaseModel):
    amount: float
    to: str = None

@app.get("/api/balance")
async def get_balance():
    print("📥 GET /api/balance called")
    return {"balance": account_balance}

@app.post("/api/transfer")
async def transfer_funds(transaction: Transaction):
    global account_balance
    print(f"📥 POST /api/transfer called with: amount={transaction.amount}, to={transaction.to}")
    if account_balance >= transaction.amount:
        account_balance -= transaction.amount
        return {"status": "success", "message": f"Transferred ${transaction.amount} to {transaction.to}"}
    else:
        return {"status": "error", "message": "Insufficient funds for transfer"}

@app.post("/api/withdraw")
async def withdraw(transaction: Transaction):
    global account_balance
    print(f"📥 POST /api/withdraw called with: amount={transaction.amount}")
    if account_balance >= transaction.amount:
        account_balance -= transaction.amount
        return {"status": "success", "message": f"Withdrew ${transaction.amount}"}
    else:
        return {"status": "error", "message": "Insufficient funds for withdrawal"}

@app.post("/api/deposit")
async def deposit(transaction: Transaction):
    global account_balance
    print(f"📥 POST /api/deposit called with: amount={transaction.amount}")
    account_balance += transaction.amount
    return {"status": "success", "message": f"Deposited ${transaction.amount}"}

@app.post("/api/loan")
async def apply_for_loan(transaction: Transaction):
    global loan_balance
    print(f"📥 POST /api/loan called with: amount={transaction.amount}")
    loan_balance += transaction.amount
    return {"status": "success", "message": f"Loan of ${transaction.amount} approved"}

@app.get("/api/credit_score")
async def get_credit_score():
    print("📥 GET /api/credit_score called")
    return {"credit_score": credit_score}

# Show API structure on startup
@app.on_event("startup")
async def show_api_details():
    print("\n📘 API ROUTES:")
    for route in app.routes:
        if isinstance(route, APIRoute):
            methods = ', '.join(route.methods)
            path = route.path
            endpoint_name = route.name
            parameters = [param.name for param in route.dependant.query_params]
            body_fields = (
                [field.name for field in route.body_field.model_fields.values()]
                if route.body_field and hasattr(route.body_field, 'model_fields')
                else []
            )

            print(f"\n🔹 Endpoint: {endpoint_name}")
            print(f"   📍 Path: {path}")
            print(f"   🚦 Methods: {methods}")
            if parameters:
                print(f"   🧾 Query Params: {parameters}")
            if body_fields:
                print(f"   📦 Body Params: {body_fields}")

# Start server
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

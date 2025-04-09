import requests

def execute_action(response):
    text = response.lower()

    if any(kw in text for kw in ["transfer", "send money", "move funds", "pay"]):
        print("💸 Simulating fund transfer...")
        # Replace with your actual endpoint and payload
        requests.post("http://localhost:8000/api/transfer", json={"amount": 500, "to": "savings"})

    elif any(kw in text for kw in ["report", "financial summary", "show summary"]):
        print("📊 Generating financial report...")
        requests.get("http://localhost:8000/api/report")

    elif any(kw in text for kw in ["balance", "how much money", "check money", "funds available"]):
        print("💰 Checking your current balance...")
        requests.get("http://localhost:8000/api/balance")

    elif any(kw in text for kw in ["withdraw", "cash out", "take out money"]):
        print("💵 Processing withdrawal request...")
        requests.post("http://localhost:8000/api/withdraw", json={"amount": 100})

    elif any(kw in text for kw in ["deposit", "add funds", "put money"]):
        print("💵 Processing deposit request...")
        requests.post("http://localhost:8000/api/deposit", json={"amount": 300})

    elif any(kw in text for kw in ["loan", "borrow", "apply for loan"]):
        print("💳 Processing loan request...")
        requests.post("http://localhost:8000/api/loan", json={"amount": 1000})

    elif any(kw in text for kw in ["credit score", "my score", "credit rating"]):
        print("🔍 Retrieving your credit score...")
        requests.get("http://localhost:8000/api/credit_score")

    elif any(kw in text for kw in ["exit", "quit", "stop", "bye"]):
        print("👋 Exiting the assistant. Have a great day!")
        exit()

    else:
        print("⚙️ No recognizable action. Awaiting clarification.")

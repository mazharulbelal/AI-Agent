import requests
import re

def extract_amount_and_target(text):
    amount_match = re.search(r"\b\d+(\.\d+)?\b", text)
    target_match = re.search(r"to\s+(\w+)", text)
    amount = float(amount_match.group()) if amount_match else 0
    target = target_match.group(1) if target_match else "default"
    return amount, target

def execute_action(response):
    text = response.lower()

    if any(kw in text for kw in ["hello", "hi", "hey"]):
        print("🤖 Hello! How can I help you, Mazharul?")

    elif "send" in text or "transfer" in text:
        amount, target = extract_amount_and_target(text)
        print(f"💸 Transferring ${amount} to {target}...")
        requests.post("http://localhost:8000/api/transfer", json={"amount": amount, "to": target})

    elif "check" in text and "balance" in text or "my balance" in text:
        print("💰 Checking your balance...")
        requests.get("http://localhost:8000/api/balance")

    elif "report" in text or "spending history" in text or "financial summary" in text:
        print("📊 Generating your financial report...")
        requests.get("http://localhost:8000/api/report")

    elif "budget" in text:
        print("📈 Budgeting feature coming soon...")

    elif "withdraw" in text:
        amount, _ = extract_amount_and_target(text)
        print(f"💵 Withdrawing ${amount}...")
        requests.post("http://localhost:8000/api/withdraw", json={"amount": amount})

    elif "deposit" in text:
        amount, _ = extract_amount_and_target(text)
        print(f"💵 Depositing ${amount}...")
        requests.post("http://localhost:8000/api/deposit", json={"amount": amount})

    elif "loan" in text or "apply for loan" in text:
        amount, _ = extract_amount_and_target(text)
        print(f"💳 Applying for a loan of ${amount}...")
        requests.post("http://localhost:8000/api/loan", json={"amount": amount})

    elif "credit score" in text:
        print("🔍 Checking your credit score...")
        requests.get("http://localhost:8000/api/credit_score")

    elif any(kw in text for kw in ["exit", "quit", "stop", "bye"]):
        print("👋 Exiting. Have a great day, Mazharul!")
        exit()

    else:
        print("🤔 I didn’t understand that. Can you repeat it differently?")

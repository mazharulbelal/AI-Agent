def execute_action(response):
    text = response.lower()

    if any(kw in text for kw in ["transfer", "send money", "move funds", "pay"]):
        print("💸 Simulating fund transfer...")
    elif any(kw in text for kw in ["report", "financial summary", "show summary"]):
        print("📊 Generating financial report...")
    elif any(kw in text for kw in ["balance", "how much money", "check money", "funds available"]):
        print("💰 Checking your current balance...")
    elif any(kw in text for kw in ["transaction", "what did i spend", "spending history", "recent activity"]):
        print("📜 Displaying your recent transactions...")
    elif any(kw in text for kw in ["loan", "borrow", "apply for loan"]):
        print("💳 Processing loan request...")
    elif any(kw in text for kw in ["account statement", "monthly statement", "bank statement"]):
        print("📝 Generating account statement...")
    elif any(kw in text for kw in ["withdraw", "take out money", "cash out"]):
        print("💵 Processing withdrawal request...")
    elif any(kw in text for kw in ["deposit", "put money", "add funds"]):
        print("💵 Processing deposit request...")
    elif any(kw in text for kw in ["budget", "spending plan", "monthly budget"]):
        print("📊 Creating your budget summary...")
    elif any(kw in text for kw in ["investment", "portfolio", "stocks", "funds"]):
        print("📈 Checking your investment portfolio...")
    elif any(kw in text for kw in ["credit score", "my score", "credit rating"]):
        print("🔍 Retrieving your credit score...")
    elif any(kw in text for kw in ["exit", "quit", "stop", "bye"]):
        print("👋 Exiting the assistant. Have a great day!")
        exit()
    else:
        print("⚙️ No recognizable action. Awaiting clarification.")

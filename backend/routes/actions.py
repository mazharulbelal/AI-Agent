import re

async def handle_action(command: str):
    command = command.lower()

    # Mock data
    balance = 1234.56
    credit_score = 750
    savings_goals = {
        "vacation": 500,
        "emergency": 1200,
    }

    # Greetings
    if any(word in command for word in ["hi", "hello", "hey", "good morning", "good evening"]):
        text = "Hello! How can I assist you with your finances today?"
        html = f"<h2>{text}</h2>"
        return text, html

    # Balance check
    elif "balance" in command:
        text = f"Your current balance is ${balance:.2f}"
        html = f"<h2>{text}</h2>"
        return text, html

    # Send / Transfer money
    elif match := re.search(r"(send|transfer)\s+\$?(\d+(\.\d{1,2})?)\s+(to|into)?\s*(.*)", command):
        amount = match.group(2)
        recipient = match.group(5) or "specified account"
        text = f"Transferred ${amount} to {recipient} successfully."
        html = f"<h2>{text}</h2>"
        return text, html

    # Deposit
    elif match := re.search(r"deposit\s+\$?(\d+(\.\d{1,2})?)", command):
        amount = match.group(1)
        text = f"${amount} deposited successfully to your account."
        html = f"<h2>{text}</h2>"
        return text, html

    # Withdraw
    elif match := re.search(r"withdraw\s+\$?(\d+(\.\d{1,2})?)", command):
        amount = match.group(1)
        text = f"${amount} withdrawn from your account."
        html = f"<h2>{text}</h2>"
        return text, html

    # Load request
    elif "load request" in command:
        text = "Load request has been processed."
        html = f"<h2>{text}</h2>"
        return text, html

    # Recent transactions
    elif "recent transactions" in command or "transaction history" in command:
        text = "Here are your last 3 transactions:"
        html = """
        <h2>Recent Transactions</h2>
        <ul>
            <li>+ $500 - Salary</li>
            <li>- $75 - Electricity Bill</li>
            <li>- $30 - Online Shopping</li>
        </ul>
        """
        return text, html

    # Account Info
    elif "account info" in command or "my account" in command:
        text = "Here's your account information."
        html = """
        <h2>Account Info</h2>
        <p>Name: Md Mazharul Islam</p>
        <p>Account Number: 1234-5678-90</p>
        <p>Account Type: Savings</p>
        <p>Status: Active</p>
        """
        return text, html

    # Credit score
    elif "credit score" in command:
        text = f"Your current credit score is {credit_score}."
        html = f"<h2>{text}</h2>"
        return text, html

    # Loan inquiry
    elif "loan" in command:
        text = "You're eligible to apply for a loan up to $10,000 with 5.5% APR."
        html = f"<h2>{text}</h2>"
        return text, html

    # Budgeting
    elif "create budget" in command or "budget" in command:
        text = "Your monthly budget of $2,000 has been set. You can start adding categories."
        html = f"<h2>{text}</h2>"
        return text, html

    # Savings goals
    elif "savings goal" in command or "my goals" in command:
        text = "Here are your savings goals:"
        html = "<h2>Savings Goals</h2><ul>"
        for goal, amount in savings_goals.items():
            html += f"<li>{goal.capitalize()}: ${amount}</li>"
        html += "</ul>"
        return text, html

    # Bill payment
    elif match := re.search(r"pay\s+\$?(\d+(\.\d{1,2})?)\s+(for\s+)?(.*)", command):
        amount = match.group(1)
        bill_type = match.group(4)
        text = f"Paid ${amount} for {bill_type}."
        html = f"<h2>{text}</h2>"
        return text, html

    # Investment inquiry
    elif "investment" in command:
        text = "Your current investment portfolio includes stocks, bonds, and crypto totaling $5,320."
        html = f"<h2>{text}</h2>"
        return text, html

    # Currency exchange
    elif "convert" in command or "exchange rate" in command:
        text = "1 USD = 110 BDT. Do you want to convert a specific amount?"
        html = f"<h2>{text}</h2>"
        return text, html

    # Financial report
    elif "financial report" in command or "monthly report" in command:
        text = "Here's your financial summary for this month."
        html = """
        <h2>Monthly Financial Report</h2>
        <p>Income: $3000</p>
        <p>Expenses: $2100</p>
        <p>Savings: $900</p>
        """
        return text, html

    # Help
    elif "help" in command or "what can you do" in command:
        text = "I can help with balance checks, transfers, deposits, withdrawals, budgeting, and more!"
        html = f"<h2>{text}</h2>"
        return text, html

    # Fallback
    else:
        text = "Sorry, I didn't understand that. Please try asking in another way."
        html = f"<h2>{text}</h2>"
        return text, html

# 💼 AI Finance Accountant Agent

### 🧑‍💻 Created by
**Md Mazharul Islam**  
🌐 http://mazharulbelal.github.io

### 🧠 What It Does
This is a smart assistant that listens to your **voice** and helps with **money-related tasks** — like sending money, checking your balance, or making reports. It uses `llama3.2` for answering and a local database (vector store) to understand your past info better.

---

### ⚙️ Setup (Step-by-step)

1. **Create a virtual environment:**
   ```bash
   python3 -m venv venv
   ```

2. **Activate the environment:**
   ```bash
   source venv/bin/activate
   ```

3. **Install all required packages:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Download the AI model:**
   ```bash
   ollama pull llama3.2
   ```

---

### ➕ Add Your Own Data (Vectors)

You can **add more finance documents or notes** to improve the assistant’s answers.

To do that:
- Put your files (like `.txt`, `.pdf`, etc.) in the `data/` folder
- Then run this command to process them:

```bash
python ingest.py
```

It will read your files and update the internal database (vector store) so the AI can use them when answering.

---

### ▶️ Start the Agent

```bash
python main.py
```

Once it starts, just **speak your command** into the mic.

---

### 🖙️ What You Can Say

Here are some example voice commands you can try:

💸 **Money Transfers**
- "Transfer 500 dollars to my savings"
- "Send money to John"
- "Move funds to another account"
- "Pay my rent"

📊 **Reports and Summaries**
- "Generate financial report for March"
- "Show me a summary of my spending"
- "Create a monthly budget"
- "Make a spending plan for this month"

💰 **Balance and Activity**
- "What's my account balance?"
- "How much money do I have?"
- "Show my recent transactions"
- "What did I spend last week?"

🏦 **Banking and Finance**
- "Withdraw 1000 dollars"
- "Deposit 300 into checking"
- "Apply for a loan"
- "Show my credit score"
- "Check my investment portfolio"

📝 **Statements**
- "Show my account statement"
- "Print my bank statement"
- "Get monthly statement"

🚪 **Exit the App**
- "Exit"
- "Stop"
- "Quit"
- "Bye"

---

### 💡 Tips

- Make sure your **microphone** is connected.
- Add more data using the `data/` folder to make answers smarter.
- Keep your commands **short and clear** for best results.

---




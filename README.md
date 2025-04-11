# 💼 AI Finance Accountant Agent

### 🧑‍💻 Created by
**Md Mazharul Islam**  
🌐 [Portfolio Website](http://mazharulbelal.github.io)

### 🎥 Tutorial
Watch the Video on YouTube:  
[![Watch the video](https://img.youtube.com/vi/Irwo242U2h4/0.jpg)](https://www.youtube.com/watch?v=Irwo242U2h4)
---

### 🧠 What It Does
This is a smart **AI-powered finance assistant** that listens to your **voice commands** and helps you with various **financial tasks**, such as sending money, checking your balance, and generating reports.

It uses `llama3.2` for intelligent response generation and a **local vector store** database to remember and use your past financial data.

---

### ⚙️ Setup Instructions

1. **Create a virtual environment:**
   ```bash
   python3 -m venv venv
   ```

2. **Activate the environment:**
   ```bash
   source venv/bin/activate
   ```

3. **Install dependencies:**
   *(If you have a `requirements.txt` file)*
   ```bash
   pip install -r requirements.txt
   ```

---


### ▶️ Start the Environment

```bash
python env.py
```


### ▶️ Start the Server

```bash
python server.py
```

Once the server is running, you can **speak directly into your microphone** to start using the assistant.

---

### 🎙️ Voice Commands You Can Try
Here are some useful commands the assistant understands:

- "Send 100 to account"
- "Transfer 200 to savings"
- "Check my balance"
- "Show spending history"
- "Make a budget"
- "Get financial report"
- "Withdraw 100"
- "Deposit 500"
- "Apply for a loan"
- "Show my credit score"

🔍 For more actions and custom phrases, check the `actions.py` file.

---

### 🔮 Future Plans

1. Design a web interface with a voice input button.
2. Add temporary OTP verification for user authentication.
3. Develop an iOS app to allow voice input directly from the device.
4. Notify users via email and push notification when a session starts or ends.
5. Send SMS/notifications when a financial transaction is completed.

---

### 💡 Tips for Best Experience

- Ensure your **microphone is properly connected**.
- Keep your voice commands **short and clear**.
- Use a quiet environment for more accurate voice detection.
---

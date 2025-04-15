# 🤖 AI Finance Agent

An intelligent voice-powered finance assistant built with FastAPI and local AI tools (LLaMA, Ollama, etc). It listens to your voice, understands financial commands, and responds both visually and with voice feedback. All logic is handled locally with API calls—no cloud AI dependencies.

🧑‍💻 Created by

### 🧑‍💻 Created by
**Md Mazharul Islam**  
🌐 [Portfolio Website](http://mazharulbelal.github.io)


---

## 🚀 Features

- 🎙️ Voice-controlled interface
- 🔐 All processing runs locally
- 🔄 Interacts with finance APIs (mock or real)
- 🗂️ HTML output responses with voice narration
- 🧠 Built-in financial command recognition with regex

---

## 🧠 Supported Voice Commands

| Emoji | Example Command |
|-------|-----------------|
| 👋 | "Hi" |
| 👤 | "My account info" |
| 💵 | "Check my balance" |
| 📤 | "Send 100 to John" |
| 🏦 | "Deposit 200" |
| 🧾 | "Show recent transactions" |
| 📊 | "Create a budget" |
| 🎯 | "Show my savings goals" |
| 💳 | "Apply for a loan" |
| 📈 | "View investment portfolio" |
| 💸 | "Pay 70 for electricity" |
| 💱 | "Convert USD to BDT" |
| 📋 | "Get my financial report" |
| 📉 | "Show my credit score" |
| 🏧 | "Withdraw 50" |
| 🆘 | "Help" |

---


## 🛠️ How to Run the Project

1. **Clone the repo:**
```bash
git clone https://github.com/mazharulbelal/AI-Agent.git
cd AI-Agent
```

2. **Create and activate a virtual environment:**
```bash
python3 -m venv venv
source venv/bin/activate
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

4. **Start the backend server:**
```bash
python -m backend.server
```

5. **Open your browser and navigate to:**
```
http://localhost:8000
```

---

## 🎙️ How to Use Voice Input

- Open `index.html` in your browser
- Click the **🔵 round mic button**
- Speak any of the supported commands (e.g., "Check my balance")
- The assistant will:
  - Transcribe your voice
  - Process the command
  - Return HTML + voice response from backend

---

## 📹 Demo (Coming Soon)
Stay tuned for a video walkthrough! 🚧

---

## ❤️ Author

Made with 💡 by [Md Mazharul Islam](https://github.com/mazharulbelal)

---

## 🧩 Powered By

- Python + FastAPI
- WebSpeech API (voice recognition)
- LLaMA / Ollama (local LLM)
- HTML5 + JavaScript for frontend
---


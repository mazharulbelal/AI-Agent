# main.py

from prompt import get_prompt_chain
from vector import retriever
from actions import execute_action
import speech_recognition as sr

def transcribe_voice():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()
    with mic as source:
        print("🎙️ Speak your command...")
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio)
        print(f"📝 You said: {text}")
        return text
    except sr.UnknownValueError:
        print("❌ Could not understand audio")
        return ""
    except sr.RequestError as e:
        print(f"❌ Recognition error: {e}")
        return ""

if __name__ == "__main__":
    chain = get_prompt_chain()
    while True:
        print("\n----------------------------")
        command = transcribe_voice()
        if command.lower() in ["stop", "exit", "q"]:
            break
        docs = retriever.invoke(question=command)  # Correctly passing the command
        response = chain.invoke({ "context": docs, "question": command })
        print(f"🤖 AI: {response}")
        execute_action(response)

from langchain_community.llms.ollama import Ollama
from langchain_core.prompts import ChatPromptTemplate

def get_prompt_chain():
    model = Ollama(model="llama3.2")
    template = """
You are a finance assistant. Based on the user's request and context, reply with the intended finance operation in plain language.

Context: {context}
User question: {question}
"""
    prompt = ChatPromptTemplate.from_template(template)
    return prompt | model
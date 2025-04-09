# vector.py

class Retriever:
    def invoke(self, question: str):
        # Simulate retrieving documents based on the question
        print(f"Retrieving docs for the question: {question}")
        return f"Documents related to: {question}"

retriever = Retriever()

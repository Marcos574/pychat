from transformers import pipeline
from llm.llm_connector import LLMConnector

class RoBERTaConnector(LLMConnector):
    def __init__(self):
        self.model = None

    def connect(self):
        print("Carregando o modelo RoBERTa para perguntas e respostas...")
        self.model = pipeline("question-answering", model="deepset/roberta-base-squad2")

    def generate_response(self, question: str, context: str) -> str:
        result = self.model(question=question, context=context)
        return result['answer']

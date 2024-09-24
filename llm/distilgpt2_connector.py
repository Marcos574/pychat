from transformers import pipeline
from llm.llm_connector import LLMConnector

class DistilGPT2Connector(LLMConnector):
    def __init__(self):
        self.model = None

    def connect(self):
        print("Carregando o modelo DistilGPT-2...")
        self.model = pipeline("text-generation", model="distilgpt2")

    def generate_response(self, prompt: str) -> str:
        response = self.model(prompt, max_length=50, num_return_sequences=1, temperature=0.7, top_k=50)
        return response[0]['generated_text']
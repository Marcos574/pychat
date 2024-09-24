import google.generativeai as genai
from llm.llm_connector import LLMConnector

class GeminiConnector(LLMConnector):
    def __init__(self, api_key: str):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-1.5-flash')

    def connect(self):
        print("Conectando à API do Gemini...")

    def generate_response(self, prompt: str) -> str:
        try:
            response = self.model.generate_content(prompt)
            return response.text if response else "Erro ao gerar resposta"
        except Exception as e:
            return f"Erro: {str(e)}"

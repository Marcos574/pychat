import openai
from llm.llm_connector import LLMConnector

class ChatGPTConnector(LLMConnector):
    def __init__(self, api_key: str):
        self.api_key = api_key
        openai.api_key = api_key
    
    def connect(self):
        print("Conectando ao ChatGPT...")

    def generate_response(self, prompt: str) -> str:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message['content'].strip()
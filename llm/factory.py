from llm.GPT_connector import ChatGPTConnector
from llm.llm_connector import LLMConnector

class LLMFactory:
    @staticmethod
    def get_llm(llm_type: str, api_key: str = None) -> LLMConnector:
        if llm_type == "ChatGPT":
            return ChatGPTConnector(api_key) 
        else:
            raise ValueError(f"Tipo de LLM desconhecido: {llm_type}")

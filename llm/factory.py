from llm.GPT_connector import ChatGPTConnector
from llm.roberta_connector import RoBERTaConnector
from llm.llm_connector import LLMConnector
from llm.distilgpt2_connector import DistilGPT2Connector
from llm.gemini_connector import GeminiConnector

class LLMFactory:
    @staticmethod
    def get_llm(llm_type: str, api_key: str = None) -> LLMConnector:
        if llm_type == "ChatGPT":
            return ChatGPTConnector(api_key)
        elif llm_type == "RoBERTa":
            return RoBERTaConnector()
        elif llm_type == "DistilGPT2":
            return DistilGPT2Connector()
        if llm_type == "Gemini":
            return GeminiConnector(api_key)    
        else:
            raise ValueError(f"Tipo de LLM desconhecido: {llm_type}")

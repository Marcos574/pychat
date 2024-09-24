from llm.GPT_connector import ChatGPTConnector
from llm.roberta_connector import RoBERTaConnector
from llm.distilgpt2_connector import DistilGPT2Connector
from llm.llm_connector import LLMConnector

class LLMFactory:
    @staticmethod
    def get_llm(llm_type: str, api_key: str = None) -> LLMConnector:
        if llm_type == "ChatGPT":
            return ChatGPTConnector(api_key)
        elif llm_type == "RoBERTa":
            return RoBERTaConnector()
        elif llm_type == "DistilGPT2":
            return DistilGPT2Connector() 
        else:
            raise ValueError(f"Tipo de LLM desconhecido: {llm_type}")

from dotenv import load_dotenv
import os
from cli.cli import CLI
from llm.gemini_connector import GeminiConnector
from llm.distilgpt2_connector import DistilGPT2Connector
from llm.roberta_connector import RoBERTaConnector

def main():
    load_dotenv()
    llm_connectors = {
        "Gemini": GeminiConnector(os.getenv('GEMINI_API_KEY')),
        "DistilGPT2": DistilGPT2Connector(),
        "RoBERTa": RoBERTaConnector(),
    }
    cli = CLI(llm_connectors)
    cli.start()

if __name__ == "__main__":
    main()

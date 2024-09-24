from abc import ABC, abstractmethod

class LLMConnector(ABC):
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def generate_response(self, prompt: str) -> str:
        pass
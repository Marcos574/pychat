from abc import ABC, abstractmethod

class EvaluationStrategy(ABC):
    @abstractmethod
    def evaluate(self, response: str) -> float:
        """
        Avalia a resposta e retorna um score.
        :param response: A resposta a ser avaliada.
        :return: Um score que representa a avaliação.
        """
        pass

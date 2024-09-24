from strategy.evaluation_strategy import EvaluationStrategy

class ClarityEvaluation(EvaluationStrategy):
    def evaluate(self, response: str) -> float:
        sentences = response.split('.')
        num_sentences = len([s for s in sentences if s.strip()])
        
        score = 1 / num_sentences if num_sentences > 0 else 0
        return score

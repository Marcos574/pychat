from strategy.evaluation_strategy import EvaluationStrategy

class AccuracyEvaluation(EvaluationStrategy):
    def evaluate(self, response: str) -> float:
        
        keywords = ["certo", "correto", "exato", "preciso"]
        keyword_count = sum(response.lower().count(keyword) for keyword in keywords)
        

        score = keyword_count / len(response.split()) if response.split() else 0
        return score

from strategy.evaluation_strategy import EvaluationStrategy

class RelevanceEvaluation(EvaluationStrategy):
    def evaluate(self, response: str) -> float:
        keywords = ["importante", "essencial", "fundamental", "notável"]
        keyword_count = sum(response.lower().count(keyword) for keyword in keywords)
        
        score = keyword_count / len(response.split()) if response.split() else 0
        return score

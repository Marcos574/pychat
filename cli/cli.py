from cli.ask_question_command import AskQuestionCommand
import re
from strategy.accuracy_evaluation import AccuracyEvaluation
from strategy.clarity_evaluation import ClarityEvaluation
from strategy.relevance_evaluation import RelevanceEvaluation
from strategy.evaluation_strategy import EvaluationStrategy

class CLI:
    def __init__(self, llm_connectors):
        self.llm_connectors = llm_connectors

    def clean_response(self, response: str) -> str:
        cleaned_response = re.sub(r'\n+', '\n', response)
        cleaned_response = cleaned_response.strip()
        return cleaned_response

    def evaluate_responses(self, responses: dict, strategy: EvaluationStrategy):
        evaluations = {}
        for model_name, response in responses.items():
            score = strategy.evaluate(response)
            evaluations[model_name] = score
        return evaluations

    def select_evaluation_strategy(self):
        print("Selecione a estratégia de avaliação:")
        print("1. Avaliação de Precisão")
        print("2. Avaliação de Clareza")
        print("3. Avaliação de Relevância")
        choice = input("Digite o número da estratégia desejada: ")

        if choice == '1':
            return AccuracyEvaluation()
        elif choice == '2':
            return ClarityEvaluation()
        elif choice == '3':
            return RelevanceEvaluation()
        else:
            print("Escolha inválida. Usando avaliação de precisão como padrão.")
            return AccuracyEvaluation()

    def send_prompt(self, prompt: str):
        command = AskQuestionCommand(self.llm_connectors, prompt)
        responses = command.execute()
        for model_name, response in responses.items():
            cleaned_response = self.clean_response(response)
            print(f"\n[{model_name}] Resposta: {cleaned_response}")

        # Seleção da estratégia de avaliação
        evaluation_strategy = self.select_evaluation_strategy()
        evaluations = self.evaluate_responses(responses, evaluation_strategy)
        
        print("\nAvaliações das respostas:")
        for model_name, score in evaluations.items():
            print(f"[{model_name}] Pontuação: {score}")

    def start(self):
        print("Bem-vindo ao CLI de LLM!")
        while True:
            prompt = input("Digite seu prompt (ou 'sair' para encerrar): ")
            if prompt.lower() == 'sair':
                break
            self.send_prompt(prompt)



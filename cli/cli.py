# cli.py

from cli.ask_question_command import AskQuestionCommand
import re

class CLI:
    def __init__(self, llm_connectors):
        self.llm_connectors = llm_connectors

    def clean_response(self, response: str) -> str:
        """
        Limpa a resposta removendo quebras de linha excessivas e espaços em branco.
        :param response: A resposta original.
        :return: A resposta limpa.
        """
        # Remove múltiplas quebras de linha e espaços em branco
        cleaned_response = re.sub(r'\n+', '\n', response)  # Substitui múltiplas quebras de linha por uma única
        cleaned_response = cleaned_response.strip()  # Remove espaços em branco no início e no final
        return cleaned_response

    def send_prompt(self, prompt: str):
        command = AskQuestionCommand(self.llm_connectors, prompt)
        responses = command.execute()
        for model_name, response in responses.items():
            cleaned_response = self.clean_response(response)
            print(f"\n[{model_name}] Resposta: {cleaned_response}")
    
    def start(self):
        print("Bem-vindo ao CLI de LLM!")
        while True:
            prompt = input("Digite seu prompt (ou 'sair' para encerrar): ")
            if prompt.lower() == 'sair':
                break
            self.send_prompt(prompt)


class AskQuestionCommand:
    def __init__(self, llm_connectors, prompt):
        """
        Inicializa o comando para enviar perguntas a diferentes modelos de LLM.
        :param llm_connectors: Dicionário de conectores de LLM.
        :param prompt: O prompt a ser enviado.
        """
        self.llm_connectors = llm_connectors
        self.prompt = prompt

    def execute(self):
        """
        Executa o comando e retorna as respostas de todos os LLMs.
        :return: Um dicionário com os nomes dos modelos como chaves e suas respostas como valores.
        """
        responses = {}
        for model_name, connector in self.llm_connectors.items():
            try:
                connector.connect()
                response = connector.generate_response(self.prompt)
                responses[model_name] = response
            except Exception as e:
                responses[model_name] = f"Erro ao obter resposta: {str(e)}"
        return responses

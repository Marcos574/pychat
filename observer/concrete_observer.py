from observer.observer_interface import Observer

class ResponseObserver(Observer):
    def update(self, data: dict):
        for model_name, response in data.items():
            print(f"Notificação: Resposta atualizada de {model_name}: {response}")

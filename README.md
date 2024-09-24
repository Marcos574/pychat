# pychat

## Visão Geral

Este projeto implementa uma interface de linha de comando (CLI) que se conecta com diferentes modelos de linguagem (LLMs), como por exemplo o Gemini, RoBERTa e DistilGPT2.
O principal objetivo é enviar prompts para esses modelos, exibir as respostas e avaliá-las utilizando diferentes estratégias, além de notificar o usuário automaticamente quando acontecer uma mudança nessas respostas, usando o padrão de design Observer.

## Funcionalidades

### 1 - Envio de prompts para vários modelos

- O CLI permite enviar um prompt que será processado por todos os modelos implementados, e então exibir as respostas de cada modelo.

### 2 - Estratégias de avaliação

- O projeto implementa as seguintes estratégias de avaliação para classificar as respostas dos modelos: **Precisão (Accuracy)**, **Clareza (Clarity)** e **Relevância (Relevance)**.

- O usuário pode escolher qual estratégia de avaliação ele deseja aplicar.

### 3 - Notificação

- O CLI notifica automaticamente com o padrão observer o usuário sempre que uma nova resposta for gerada pelos LLMs.

## Estrutura do projeto

- cli/ : Contém o código principal do CLI e o comando para executar perguntas. Implementado com o design pattern "Command".

- llm/ : Contém os conectores para diferentes LLMs (Gemini, DistilGPT2, RoBERTa). Implementado com o design pattern "Factory".

- observer/ : Implementa o padrão Observer, responsável por notificar o cliente sobre atualizações nas respostas.

- strategy/ : Implementa as estratégias de avaliação que podem ser escolhidas pelo usuário. Implementado com o design pattern "strategy".

## Pré-requisitos

1 - Python 3.7+

2 - Bibliotecas python (especificadas no requirements.txt)

3 - Chave da API do Gemini. Você pode configurá-la no arquivo .env

## Configuração

### 1 - Clone o repositório

```
git clone https://github.com/Marcos574/pychat.git
cd pychat
```

### 2 - Instale as dependências

```
pip install -r requirements.txt
```

### 3 - Crie um arquivo .env na raiz do projeto e adicione sua chave da API do Gemini:

```
GEMINI_API_KEY=your_gemini_api_key_here
```

## Execução

### 1 - iniciar o CLI:

Para iniciar a interface de linha de comando, execute o seguinte comando:

```
python main.py
```

### 2 - Envio de prompts

- Após iniciar o CLI, você pode inserir prompts que serão enviados para os LLMs disponíveis

- O CLI exibirá as respostas de cada modelo

### 3 - Escolha da estratégia de avaliação

- Após as respostas serem apresentadas, o CLI solicitará que você escolha uma das três estratégias de avaliação

## Vídeo da aplicação em execução

- Segue o vídeo explicando e executando brevemente a aplicação: [vídeo](https://youtu.be/n3PoU3X1GAQ)

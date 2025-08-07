from crewai import Agent
from crewai_tools import SerperDevTool
from textwrap import dedent
# Remova a importação do ChatOpenAI e adicione a do ChatGroq
# from langchain_openai import ChatOpenAI 
from langchain_groq import ChatGroq 
import yaml
import os

# Carregar configurações dos agentes do arquivo YAML
with open('./config/agents.yaml', 'r') as file:
    agents_config = yaml.safe_load(file)

# Instanciar a ferramenta de pesquisa
search_tool = SerperDevTool()

# Instanciar o LLM da Groq que será usado por todos os agentes
# Você pode escolher outros modelos, como 'mixtral-8x7b-32768'
llm = ChatGroq(
    api_key=os.environ.get("GROQ_API_KEY"),
    model_name="compound-beta"
)

class EnemAgents:
    def pesquisador_sociocultural(self):
        config = agents_config['pesquisador_sociocultural']
        return Agent(
            role=config['role'],
            goal=config['goal'],
            backstory=dedent(config['backstory']),
            tools=[search_tool],
            verbose=config.get('verbose', True),
            llm=llm # Passa o modelo da Groq para o agente
        )

    def redator_enem(self):
        config = agents_config['redator_enem']
        return Agent(
            role=config['role'],
            goal=config['goal'],
            backstory=dedent(config['backstory']),
            verbose=config.get('verbose', True),
            llm=llm # Passa o modelo da Groq para o agente
        )

    def avaliador_especialista(self):
        config = agents_config['avaliador_especialista']
        return Agent(
            role=config['role'],
            goal=config['goal'],
            backstory=dedent(config['backstory']),
            verbose=config.get('verbose', True),
            llm=llm # Passa o modelo da Groq para o agente
        )
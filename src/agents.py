from crewai import Agent
from crewai_tools import SerperDevTool
from textwrap import dedent
from langchain_openai import ChatOpenAI
import yaml

# Carregar configurações dos agentes do arquivo YAML
with open('./config/agents.yaml', 'r') as file:
    agents_config = yaml.safe_load(file)

# Instanciar a ferramenta de pesquisa
search_tool = SerperDevTool()

class EnemAgents:
    def pesquisador_sociocultural(self):
        config = agents_config['pesquisador_sociocultural']
        return Agent(
            role=config['role'],
            goal=config['goal'],
            backstory=dedent(config['backstory']),
            tools=[search_tool],
            verbose=config.get('verbose', True),
            llm=ChatOpenAI() # Pode ser configurado para usar o modelo do.env
        )

    def redator_enem(self):
        config = agents_config['redator_enem']
        return Agent(
            role=config['role'],
            goal=config['goal'],
            backstory=dedent(config['backstory']),
            verbose=config.get('verbose', True),
            llm=ChatOpenAI()
        )

    def avaliador_especialista(self):
        config = agents_config['avaliador_especialista']
        return Agent(
            role=config['role'],
            goal=config['goal'],
            backstory=dedent(config['backstory']),
            verbose=config.get('verbose', True),
            llm=ChatOpenAI()
        )
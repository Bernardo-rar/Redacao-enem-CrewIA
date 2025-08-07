import os
from crewai import Agent, Task, Crew, Process
from crewai_tools import SerperDevTool

# Defina sua chave de API da Serper como uma variável de ambiente
# os.environ = "SUA_CHAVE_AQUI"

# Crie uma ferramenta de busca
search_tool = SerperDevTool()

# Crie um agente de pesquisa
researcher = Agent(
  role='Pesquisador Sênior',
  goal='Descobrir tecnologias de ponta em IA e ciência de dados',
  backstory="""Você é um pesquisador sênior em uma renomada instituição de tecnologia.
  Sua especialidade é identificar tendências emergentes e explicar seu impacto.""",
  verbose=True,
  allow_delegation=False,
  tools=[search_tool]
)

# Crie uma tarefa para o agente
task1 = Task(
  description="""Investigue as últimas tendências em Modelos de Linguagem de Grande Escala (LLMs) em 2024.
  Identifique três tendências principais e resuma-as.""",
  expected_output="Um relatório completo de uma página com as três principais tendências de LLMs.",
  agent=researcher
)

# Crie a equipe (crew) com o agente e a tarefa
crew = Crew(
  agents=[researcher],
  tasks=[task1],
  process=Process.sequential,
  verbose=2
)

# Inicie a execução da equipe
print("Iniciando a execução da equipe...")
result = crew.kickoff()

print("\n\n########################")
print("## Resultado Final:")
print("########################")
print(result)
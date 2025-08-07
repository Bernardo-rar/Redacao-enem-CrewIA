import os
from crewai import Agent, Task, Crew, Process
from langchain_groq import ChatGroq

# --- PASSO 1: CONFIGURAR O MODELO DE LINGUAGEM (LLM) ---
# Certifique-se de que a variável de ambiente GROQ_API_KEY está definida.
# Você pode obter uma chave gratuita em: https://console.groq.com/keys
try:
    llm = ChatGroq(
        model_name="compound-beta", # Ou outro modelo como "mixtral-8x7b-32768"
        groq_api_key=os.environ.get("GROQ_API_KEY")
    )
except Exception as e:
    print("Erro ao inicializar o LLM da Groq. Verifique se a variável de ambiente GROQ_API_KEY está definida corretamente.")
    print(e)
    exit()

# --- PASSO 2: DEFINIR O AGENTE ---
# Este agente não usa ferramentas externas; ele usa o conhecimento do LLM da Groq.
knowledge_synthesizer = Agent(
  role='Especialista em IA',
  goal='Explicar conceitos complexos de IA de forma clara e concisa',
  backstory="""Você é um especialista em Inteligência Artificial com um talento especial
  para destilar tópicos difíceis em explicações compreensíveis. Você se baseia
  em seu vasto conhecimento treinado para gerar respostas.""",
  verbose=True,
  allow_delegation=False,
  llm=llm  # Atribui o LLM da Groq diretamente ao agente
  # Note que o parâmetro 'tools' foi removido
)

# --- PASSO 3: DEFINIR A TAREFA ---
# A tarefa foi ajustada para não depender de pesquisa em tempo real.
task1 = Task(
  description="""Explique o conceito de "Mixture of Experts" (MoE) no contexto de
  Modelos de Linguagem de Grande Escala (LLMs). Como essa arquitetura funciona
  e quais são suas principais vantagens?""",
  expected_output="""Um relatório de 3 parágrafos explicando o que é MoE,
  seu funcionamento com roteamento de tokens e suas vantagens, como
  eficiência computacional.""",
  agent=knowledge_synthesizer
)

# --- PASSO 4: CRIAR E EXECUTAR A EQUIPE (CREW) ---
crew = Crew(
  agents=[knowledge_synthesizer],
  tasks=[task1],
  process=Process.sequential,
  verbose=2
)

print("Iniciando a execução da equipe com Groq...")
result = crew.kickoff()

print("\n\n########################")
print("## Resultado Final:")
print("########################")
print(result)
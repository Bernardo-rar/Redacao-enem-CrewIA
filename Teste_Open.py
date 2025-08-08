import os
from crewai import Agent, Task, Crew, Process
from langchain_openai import ChatOpenAI # <-- MUDANÇA: Importa a classe da OpenAI
from dotenv import load_dotenv

load_dotenv()

# --- PASSO 1: CONFIGURAR O MODELO DE LINGUAGEM (LLM) ---
# O código agora espera a variável de ambiente OPENAI_API_KEY.
# Você pode gerenciar suas chaves em: https://platform.openai.com/api-keys
try:
    # MUDANÇA: Substituímos ChatGroq por ChatOpenAI e ajustamos o modelo
    llm = ChatOpenAI(
        model_name="gpt-3.5-turbo", # Modelo mais custo-efetivo da OpenAI
        temperature=0.1 # Opcional: ajusta a criatividade da resposta
    )
except Exception as e:
    print("Erro ao inicializar o LLM da OpenAI. Verifique se a variável de ambiente OPENAI_API_KEY está definida corretamente.")
    print(e)
    exit()

# --- PASSO 2: DEFINIR O AGENTE (Nenhuma mudança aqui) ---
# O agente continua o mesmo, mas agora usará o poder do GPT-3.5.
knowledge_synthesizer = Agent(
    role='Especialista em IA',
    goal='Explicar conceitos complexos de IA de forma clara e concisa',
    backstory="""Você é um especialista em Inteligência Artificial com um talento especial
    para destilar tópicos difíceis em explicações compreensíveis. Você se baseia
    em seu vasto conhecimento treinado para gerar respostas.""",
    verbose=True,
    allow_delegation=False,
    llm=llm  # Atribui o LLM da OpenAI diretamente ao agente
)

# --- PASSO 3: DEFINIR A TAREFA (Nenhuma mudança aqui) ---
task1 = Task(
    description="""Explique o conceito de "Mixture of Experts" (MoE) no contexto de
    Modelos de Linguagem de Grande Escala (LLMs). Como essa arquitetura funciona
    e quais são suas principais vantagens?""",
    expected_output="""Um relatório de 3 parágrafos explicando o que é MoE,
    seu funcionamento com roteamento de tokens e suas vantagens, como
    eficiência computacional.""",
    agent=knowledge_synthesizer
)

# --- PASSO 4: CRIAR E EXECUTAR A EQUIPE (CREW) (Nenhuma mudança aqui) ---
crew = Crew(
    agents=[knowledge_synthesizer],
    tasks=[task1],
    process=Process.sequential,
    verbose=True
)

print("Iniciando a execução da equipe com OpenAI (gpt-3.5-turbo)...")
result = crew.kickoff()

print("\n\n########################")
print("## Resultado Final:")
print("########################")
print(result)
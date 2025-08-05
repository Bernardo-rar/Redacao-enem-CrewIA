from crewai import Crew, Process
from.agents import EnemAgents
from.tasks import EnemTasks
import os

# Carregar variáveis de ambiente
from dotenv import load_dotenv
load_dotenv()

class EnemCrew:
    def __init__(self, topic):
        self.topic = topic
        self.agents = EnemAgents()
        self.tasks = EnemTasks()

    def run(self):
        # Instanciar os agentes
        pesquisador = self.agents.pesquisador_sociocultural()
        redator = self.agents.redator_enem()
        avaliador = self.agents.avaliador_especialista()

        # Instanciar as tarefas
        task_pesquisa = self.tasks.pesquisa_de_tema(pesquisador, self.topic)
        task_escrita = self.tasks.escrita_da_redacao(redator, [task_pesquisa], self.topic)
        task_avaliacao = self.tasks.avaliacao_da_redacao(avaliador, [task_escrita])

        # Montar a Crew com um processo sequencial
        crew = Crew(
            agents=[pesquisador, redator, avaliador],
            tasks=[task_pesquisa, task_escrita, task_avaliacao],
            process=Process.sequential,
            verbose=2
        )

        result = crew.kickoff()
        return result

# Ponto de entrada para execução
if __name__ == "__main__":
    print("## Bem-vindo à Equipe de IA para Redação do ENEM")
    print('--------------------------------------------------')
    topic_input = input("Qual é o tema da redação que você deseja trabalhar hoje?\n")
    
    enem_crew = EnemCrew(topic_input)
    final_result = enem_crew.run()
    
    print("\n\n########################")
    print("## Tarefa Concluída!")
    print("########################\n")
    print("Resultado Final:")
    print(final_result)
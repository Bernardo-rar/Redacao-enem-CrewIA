from crewai import Task
from textwrap import dedent
import yaml

# Carregar configurações das tarefas do arquivo YAML
with open('./config/tasks.yaml', 'r') as file:
    tasks_config = yaml.safe_load(file)

class EnemTasks:
    def pesquisa_de_tema(self, agent, topic):
        config = tasks_config['pesquisa_de_tema']
        return Task(
            description=dedent(config['description'].format(topic=topic)),
            expected_output=dedent(config['expected_output']),
            agent=agent
        )

    def escrita_da_redacao(self, agent, context, topic):
        config = tasks_config['escrita_da_redacao']
        return Task(
            description=dedent(config['description'].format(topic=topic)),
            expected_output=dedent(config['expected_output']),
            agent=agent,
            context=context
        )

    def avaliacao_da_redacao(self, agent, context):
        config = tasks_config['avaliacao_da_redacao']
        return Task(
            description=dedent(config['description']),
            expected_output=dedent(config['expected_output']),
            agent=agent,
            context=context,
            output_json=True # Especifica que a saída deve ser um JSON
        )
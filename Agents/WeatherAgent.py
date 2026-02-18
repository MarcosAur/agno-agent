from agno.models.openrouter import OpenRouterResponses
from agno.agent import Agent
from dotenv import load_dotenv
from agno.tools.duckduckgo import DuckDuckGoTools

load_dotenv()

def get_weather_tool(city: str) -> dict:
    """
    Função que recebe uma cidade e consulta os dados meteorológicos referentes à essa cidade.

    Args:
        city (str): O nome da cidade solicitada.

    Returns:
        dict: Uma lista com os dados da cidade.
    """

    return {
        'city': city,
        'temperatura': '24°',
        'umidade': '10'
    }

agent = Agent(
    id='meteorologist',
    name='meteorologist',
    model=OpenRouterResponses('arcee-ai/trinity-large-preview:free'),
    tools=[get_weather_tool, DuckDuckGoTools()],
    instructions=[
        "Utilize as roles disponíveis para responder às requisições do cliente",
        "Responda de forma assertiva em um json estruturado",
        "Não crie links ou informações falsas"
    ]
)

# agent.print_response('Quero saber a previsão do tempo para fortaleza')
agent.print_response('Onde fica a cidade de fortaleza')

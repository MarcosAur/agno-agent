from agno.agent import Agent
from dotenv import load_dotenv
from agno.models.openrouter import OpenRouterResponses
from models.Order import Order

load_dotenv()

agent = Agent(
    id='garcom',
    name='Garcom',
    model=OpenRouterResponses('arcee-ai/trinity-large-preview:free'),
    role="""Você é um garçom em um restaurante que vende apenas comida. Sua função é receber uma solicitação 
    do cliente e repassa-lá aos responsáveis por cozinhar o pedido""",
    output_schema=Order,
)

agent.print_response("""Oi, bom dia. Gostaria de pedir 3 X-bugers. Dois completos e 1 sem cebola e sem picles. Quero tambem 3 batatas fritas médias e um mil shake""")

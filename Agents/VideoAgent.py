from agno.agent import Agent
from agno.models.openrouter import OpenRouterResponses
from agno.tools.duckduckgo import DuckDuckGoTools
from dotenv import load_dotenv
import os

load_dotenv()

# Agente 2 - Crítico de cinema
critic_agent = Agent(
    name="Crítico de Cinema",
    role="Buscar críticas, notas e opiniões sobre o filme.",
    model=OpenRouterResponses('arcee-ai/trinity-large-preview:free'),
    tools=[DuckDuckGoTools()],
    instructions=[
        "Pesquise por críticas profissionais e notas de usuários (IMDb, Rotten Tomatoes, Metacritic, etc.)",
        "Traga opiniões relevantes sobre a recepção do filme",
    ],
    markdown=True,
)

# Agente 3 - Analista geral da obra
analyst_agent = Agent(
    name="Analista de Obra",
    role="Analisar o significado da obra e detalhar personagens.",
    model=OpenRouterResponses('arcee-ai/trinity-large-preview:free'),
    tools=[DuckDuckGoTools()],
    instructions=[
        "Faça uma análise profunda sobre o que o autor quis dizer com a obra (temas, simbolismos)",
        "Descreva os personagens principais e seus arcos",
    ],
    markdown=True,
)

def consult_critic(query: str) -> str:
    """
    Consulta o Crítico de Cinema para obter críticas, notas e opiniões.
    
    Args:
        query (str): O que você deseja saber do crítico.
        
    Returns:
        str: A resposta do crítico.
    """
    response = critic_agent.run(query, stream=False)
    try:
        return response.content
    except AttributeError:
        return str(response)

def consult_analyst(query: str) -> str:
    """
    Consulta o Analista de Obra para obter análises profundas e detalhes de personagens.
    
    Args:
        query (str): O que você deseja saber do analista.
        
    Returns:
        str: A resposta do analista.
    """
    response = analyst_agent.run(query, stream=False)
    try:
        return response.content
    except AttributeError:
        return str(response)

def save_script(script_content: str, title: str):
    """
    Salva o roteiro gerado em um arquivo de texto na pasta 'output'.
    
    Args:
        script_content (str): O conteúdo do roteiro.
        title (str): O título descritivo para o arquivo (sem extensão).
    """
    output_dir = "output"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Sanitiza o título para ser um nome de arquivo válido
    safe_title = "".join([c for c in title if c.isalnum() or c in (' ', '-', '_')]).strip()
    filename = f"{output_dir}/{safe_title}.txt"
    
    with open(filename, "w", encoding="utf-8") as f:
        f.write(script_content)
    
    return f"Roteiro salvo com sucesso em: {filename}"

# Agente 1 - Roteirista (Líder do time)
scriptwriter_agent = Agent(
    name="Roteirista",
    role="Compilar todos os dados dos outros agentes em um texto coeso e salvar em arquivo.",
    model=OpenRouterResponses('arcee-ai/trinity-large-preview:free'),
    tools=[consult_critic, consult_analyst, save_script],
    instructions=[
        "Você é o responsável por criar o relatório final.",
        "Use a ferramenta 'consult_critic' para obter informações sobre a recepção do filme.",
        "Use a ferramenta 'consult_analyst' para obter a análise profunda e de personagens.",
        "Compile tudo em um texto bem estruturado e fluído em português.",
        "Ao final, crie um título descritivo para o episódio e use a ferramenta 'save_script' para salvar o conteúdo gerado.",
        "O título deve ser curto e representativo do conteúdo analisado."
    ],
    markdown=True,
)

if __name__ == "__main__":
    # Exemplo de uso
    scriptwriter_agent.print_response("Faça uma análise completa sobre o primeiro capítulo do manga de hajime no ippo", stream=True)

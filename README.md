# Agno Agent - Projeto de Estudos

Este repositório contém um projeto de estudos focado na exploração e compreensão do framework **Agno** para o desenvolvimento de agentes de Inteligência Artificial em Python.

O objetivo principal é entender como criar agentes autônomos, definir suas funções (roles), integrar ferramentas (tools) e estruturar as saídas de dados utilizando Pydantic.

## Estrutura do Projeto

O projeto está organizado da seguinte forma:

- **`Agents/`**: Contém a implementação dos agentes especializados.
  - `OrderAgent.py`: Um agente que atua como garçom, processando pedidos de clientes e retornando uma estrutura de dados JSON validada.
  - `WeatherAgent.py`: Um agente meteorologista que demonstra o uso de ferramentas personalizadas e integração com ferramentas externas (DuckDuckGo).
- **`models/`**: Definições de modelos de dados utilizando Pydantic para garantir a tipagem e estrutura das respostas dos agentes.
  - `Order.py`: Modelo principal do pedido.
  - `OrderItem.py`: Modelo para itens individuais de um pedido.
- **`main.py`**: Arquivo principal contendo exemplos básicos de inicialização de agentes e modelos.

## Funcionalidades Exploradas

### 1. Agentes com Roles Definidas
Utilização do parâmetro `role` para definir a persona e o objetivo do agente (ex: Garçom, Meteorologista).

### 2. Structured Output (Saída Estruturada)
Integração com o **Pydantic** para forçar o modelo de linguagem a retornar dados estruturados e validados, facilitando a integração com outros sistemas. Exemplo no `OrderAgent`.

### 3. Tool Use (Uso de Ferramentas)
Implementação de funções Python como ferramentas que o agente pode invocar.
- **Ferramentas Personalizadas**: Exemplo `get_weather_tool` no `WeatherAgent`.
- **Ferramentas Prontas**: Uso do `DuckDuckGoTools` para buscas na web.

## Tecnologias Utilizadas

- **Python 3.x**
- **[Agno](https://github.com/agno-agi/agno)**: Framework para orquestração de agentes.
- **Pydantic**: Validação de dados e definição de schemas.
- **OpenRouter / OpenAI API**: Provedores de modelos de linguagem (LLMs).
- **Python Dotenv**: Gerenciamento de variáveis de ambiente.

## Como Executar

1. **Clone o repositório:**
   ```bash
   git clone <url-do-repositorio>
   cd AgnoAgent
   ```

2. **Crie e ative um ambiente virtual:**
   ```bash
   python -m venv venv
   # Linux/Mac
   source venv/bin/activate
   # Windows
   venv\Scripts\activate
   ```

3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure as variáveis de ambiente:**
   Renomeie o arquivo `.env.example` para `.env` e adicione suas chaves de API (ex: OpenRouter, OpenAI).

5. **Execute os agentes:**
   Você pode executar os scripts individuais dentro da pasta `Agents` para testar cada funcionalidade:
   ```bash
   python Agents/OrderAgent.py
   python Agents/WeatherAgent.py
   ```

## Notas de Estudo

Este projeto é um "work in progress" e serve como base de conhecimento para funcionalidades avançadas do Agno, como memória, armazenamento vetorial e orquestração de múltiplos agentes.

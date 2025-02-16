from langchain_groq import ChatGroq
from langgraph_supervisor import create_supervisor
from langgraph.prebuilt import create_react_agent
from tools import add, subtract, multiply, divide, get_author

def get_base_LLM() -> ChatGroq:
    """
    PURPOSE: Initialize a Chat model to serve as the base LLM
    ARGUMENT: None
    RETURN: (ChatGroq): A chat model
    """
    return ChatGroq(model="llama3-70b-8192")

def get_supervisor_agent():
    """
    PURPOSE: Initialize a supervisor agent for managing agents
    ARGUMENT: None
    RETURN: (StateGraph): A supervisor agent for managing agents
    """
    return create_supervisor(agents=[get_math_agent(), get_research_agent()],
                             model=get_base_LLM(),
                             output_mode="last_message",
                             prompt="""You are a team supervisor managing a research expert and a math expert.
                             For math problems, use math_agent.
                             For questions no other agent can answer, use research_agent.
                             """)

def get_math_agent():
    """
    PURPOSE: Initialize an agent for handling basic math problems
    ARGUMENT: None
    RETURN: A math agent
    """
    return create_react_agent(model=get_base_LLM(),
                              tools=[add, subtract, multiply, divide],
                              name="math_expert",
                              prompt="You are a math expert. Always use one tool at a time")

def get_research_agent():
    """
    PURPOSE: Initialize an agent for handling research problems
    ARGUMENT: None
    RETURN: A research agent
    """
    return create_react_agent(model=get_base_LLM(),
                              tools=[get_author],
                              name="research_expert",
                              prompt="You are a world class researcher with access to the web search. Do not do any math.")

def print_results(result: dict) -> str:
    """
    PURPOSE: Print the log of actions conducted to respond to the user's prompt 
    ARGUMENT: result (dict): The complete Human and AI message
    RETURN: None
    """
    for message in result["messages"]: print(f"A.N.N.A.: {message.content}")

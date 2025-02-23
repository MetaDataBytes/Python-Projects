from langchain_groq import ChatGroq
from langgraph_supervisor import create_supervisor
from Math_agent import get_math_agent
from Research_agent import get_research_agent

def get_supervisor_agent():
    """
    PURPOSE: Initialize a supervisor agent for managing agents
    ARGUMENT: None
    RETURN: (StateGraph): A supervisor agent for managing agents
    """
    return create_supervisor(agents=[get_math_agent(), get_research_agent()],
                             model=ChatGroq(model="llama3-70b-8192"),
                             output_mode="last_message",
                             prompt="""You are a team supervisor managing several agents.
                             For math problems, use the Math Agent.
                             For questions no other agent can answer, use the Research Agent.
                             """)

def print_results(result: dict[str]) -> str:
    """
    PURPOSE: Print the log of actions conducted to respond to the user's prompt 
    ARGUMENT: result (dict): The complete Human and AI message
    RETURN: None
    """
    for message in result["messages"]: print(f"A.N.N.A.: {message.content}")
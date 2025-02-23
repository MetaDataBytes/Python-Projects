from langchain_groq import ChatGroq
from langgraph_supervisor import create_supervisor
from Math_agent import get_math_agent
from Research_agent import get_research_agent

def get_supervisor_agent():
    """
    PURPOSE: Initialize a supervisor agent for managing agents\n
    ARGUMENT: None\n
    RETURN: (StateGraph): A supervisor agent for managing agents\n
    """
    return create_supervisor(agents=[get_math_agent(), get_research_agent()],
                             model=ChatGroq(model="llama3-70b-8192"),
                             output_mode="last_message",
                             prompt="""You are a team supervisor managing several agents.
                             For math problems, use the Math Agent.
                             For questions no other agent can answer, use the Research Agent.
                             """)

def print_introduction() -> None:
    """
    PURPOSE: Print the introduction to the user\n
    ARGUMENT: None\n
    RETURN: None\n
    """
    print("""A.N.N.A.: Howdy!
          I'm an AI assistant that can answer qustions and take action.
          What can I DO for you today?
          
          You can respond with 'quit' to exit.""", end="\n\n")

def print_response(result: dict[str]) -> None:
    """
    PURPOSE: Print the log of actions conducted to respond to the user's prompt\n 
    ARGUMENT: result (dict): The complete Human and AI message\n
    RETURN: None\n
    """
    for message in result["messages"]: print(f"A.N.N.A.: {message.content}")
    print("\n")

def print_goodbye() -> None:
    """
    PURPOSE: Print goodbye to the user\n
    ARGUMENT: None\n
    RETURN: None\n
    """
    print("Goodbye! --A.N.N.A.")
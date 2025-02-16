from langchain_groq import ChatGroq
from langgraph.prebuilt import create_react_agent

def get_research_agent():
    """
    PURPOSE: Initialize an agent for handling research problems
    ARGUMENT: None
    RETURN: A research agent
    """
    return create_react_agent(model=ChatGroq(model="llama3-70b-8192"),
                              tools=[get_author],
                              name="Research Agent",
                              prompt="You are a world class researcher with access to the web search.")

def get_author(query: str) -> str:
    """
    PURPOSE: Get the name of the author of this code
    ARGUMENT: query (str): NOT USED
    RETURN: (str): The name of the author of this code
    """
    return "Justin Osborne"
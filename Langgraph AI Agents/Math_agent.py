from langchain_groq import ChatGroq
from langgraph.prebuilt import create_react_agent

def get_math_agent():
    """
    PURPOSE: Initialize an agent for handling basic math problems
    ARGUMENT: None
    RETURN: A math agent
    """
    return create_react_agent(model=ChatGroq(model="llama3-70b-8192"),
                              tools=[add, subtract, multiply, divide],
                              name="Math Agent",
                              prompt="You are a math expert.")

def add(a: float, b: float) -> float:
    """
    PURPOSE: Add a and b
    ARGUMENT: a (float), b (float)
    RETURN: (float): the sum of a (float) and b (float)
    """
    return a + b

def subtract(a: float, b: float) -> float:
    """
    PURPOSE: Subtract a (float) and b (float)
    ARGUMENT: a (float), b (float)
    RETURN: The difference of a (float) and b (float)
    """
    return a - b

def multiply(a: float, b: float) -> float:
    """
    PURPOSE: Multiply a (flaot) and b (float)
    ARGUMENT: a (flaot), b (flaot)
    RETURN: The product of a (float) and b(float)
    """
    return a * b

def divide(a: float, b: float) -> float:
    """
    PURPOSE: Divide a (float) by b (float)
    ARGUMENT: a (float), b (float)
    RETURN: The quotient of a (float) and b (float)
    """
    return a / b
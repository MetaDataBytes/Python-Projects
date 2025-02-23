from typing import Union
from langchain_groq import ChatGroq
from langgraph.prebuilt import create_react_agent

def get_math_agent():
    """
    PURPOSE: Initialize an agent for handling basic math problems\n
    ARGUMENT: None\n
    RETURN: A math agent\n
    """
    return create_react_agent(model=ChatGroq(model="llama3-70b-8192"),
                              tools=[add, subtract, multiply, divide],
                              name="Math Agent",
                              prompt="You are a math expert.")

def add(a: Union[float, int], b: Union[float, int]) -> Union[float, int]:
    """
    PURPOSE: Add a and b\n
    ARGUMENT: a (float), b (float)\n
    RETURN: (float): the sum of a and b\n
    """
    return a + b

def subtract(a: Union[float, int], b: Union[float, int]) -> Union[float, int]:
    """
    PURPOSE: Subtract a and b \n
    ARGUMENT: a (float), b (float)\n
    RETURN: The difference of a and b\n
    """
    return a - b

def multiply(a: Union[float, int], b: Union[float, int]) -> Union[float, int]:
    """
    PURPOSE: Multiply a and b\n
    ARGUMENT: a (float), b (float)\n
    RETURN: The product of a and b\n
    """
    return a * b

def divide(a: Union[float, int], b: Union[float, int]) -> Union[float, int]:
    """
    PURPOSE: Divide a by b\n
    ARGUMENT: a (float), b (float)\n
    RETURN: The quotient of a and b\n
    """
    return a / b
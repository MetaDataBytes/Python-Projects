from langchain_groq import ChatGroq

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

def get_author(query: str) -> str:
    """
    PURPOSE: Get the name of the author of this code
    ARGUMENT: query (str): NOT USED
    RETURN: (str): The name of the author of this code
    """
    return "Justin Osborne"

def general_question(query: str) -> str:
    """
    PURPOSE: The default tool to use when no other tool is approprate.
    ARGUMENT: query (str)
    RETURN: (str): The response to the query
    """
    llm = ChatGroq(model="llama3-70b-8192")
    return llm(messages=query, temperature=0)
import ollama
import db_func

def ask_ollama(question: str) -> str:
    """
    PURPOSE: Uses the Ollama API to generate an answer to a question based on relevant research from the database.\n
    ARGUMENTS: question (str): The question to be answered.\n
    RETURNS: str: The generated answer from the Ollama model.\n
    """
    return ollama.generate(
        model="llama3:8b-instruct-q4_K_M",
        prompt=(f"""
                You are a helpful assistant that accurately answers questions based on provided research.
                You do not have access to any information outside of the research.
                If the research does not contain the answer, respond with 'I don't know'.
                RESEARCH: {db_func.perform_vector_search(question=question)}\n\nQUESTION: {question}"""
        )
    )['response']
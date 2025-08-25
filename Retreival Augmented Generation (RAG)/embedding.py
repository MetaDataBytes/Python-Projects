from pdfminer.high_level import extract_text
from langchain.text_splitter import RecursiveCharacterTextSplitter
import ollama


def get_chunks(filepath: str) -> list[str]:
    """
    PURPOSE: Splits the text of a PDF into manageable chunks for processing and embedding.\n
    ARGUMENTS: filepath (str): filepath of the PDF book.\n
    RETURNS: list: A list of text chunks.
    """
    return RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200,).split_text(extract_text(filepath))

def get_embedding(chunks: list) -> list[float]:
    """
    PURPOSE: Generates embeddings for a list of text chunks using the Ollama API.\n
    ARGUMENTS: chunks (list): A list of text chunks.\n
    RETURNS: list: A list of embeddings corresponding to the text chunks.
    """
    return ollama.embed(model="mxbai-embed-large", input=chunks)['embeddings']
import re
from pypdf import PdfReader
from pdfminer.high_level import extract_text
import embedding


def get_pdf_details(filepath: str = None) -> dict[str, str, str, str, list[str], list[float]]:
    """
    PURPOSE: Extracts book metadata and text chunks from a PDF filepath, then generates embeddings for each chunk.\n
    ARGUMENTS: filepath (str): filepath of the PDF book. Defaults to None.\n
    RETURNS: dict: A dictionary containing book metadata, text chunks, and their embeddings.
    """
    reader = PdfReader(filepath)

    try:
        isbn = re.findall(r'ISBN[-–:\s]*((?:97[89][-–]?\d{1,5}[-–]?\d{1,7}[-–]?\d{1,7}[-–]?\d{1}))', extract_text(filepath))[0].replace('-', '').replace('–', '')
        title = reader.metadata.title
        author_first_name = reader.metadata.author.strip().split()[0]
        author_last_name = reader.metadata.author.strip().split()[-1] 
        chunks = embedding.get_chunks(filepath=filepath) 
        embedded_chunks = embedding.get_embedding(chunks=chunks)
        
        return {
            "ISBN": isbn, 
            "TITLE": title, 
            "AUTHOR_FIRST_NAME": author_first_name, 
            "AUTHOR_LAST_NAME": author_last_name, 
            "CHUNKS": chunks, 
            "EMBEDDED_CHUNKS": embedded_chunks
        }
    except Exception as e: 
        print("Failed to extract PDF details, skipping database insertion", end="\n\n")
        return list()
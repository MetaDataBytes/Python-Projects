import pyodbc
import ollama
import os
import pdf
import ask_ai
from dotenv import load_dotenv
from typing import List
load_dotenv()



def get_database_connection_string() -> str:
    """
    PURPOSE: Constructs the database connection string for SQL Server.\n
    ARGUMENTS: None\n
    RETURNS: str: The database connection string.
    """
    return f"DRIVER=ODBC Driver 18 for SQL Server;SERVER={os.getenv('SERVER')};DATABASE={os.getenv('DATABASE')};Trusted_Connection=yes;TrustServerCertificate=yes;"

def load_pdf_to_db_menu() -> None:
    """
    PURPOSE: Menu to load a single PDF file or multiple PDF files from a directory to the database.\n
    ARGUMENTS: filepath (str): The path to the PDF file or directory.\n
    RETURNS: None
    """
    print("Do you want to load a single PDF file to the database or multiple files from a directory?")
    print("1. Single PDF file")
    print("2. Multiple PDF files from a directory")
    print("3. Go back to main menu")
    sub_choice = input("Enter your choice: ")
    if sub_choice == '1': load_pdf_to_db(input("Enter the PDF filepath: "))
    elif sub_choice == '2':
        directory = input("Enter the directory path: ")
        for filename in os.listdir(directory):
            if filename.lower().endswith('.pdf'):
                filepath = os.path.join(directory, filename)
                print(f"Loading {filepath} to database...", end='\n')
                load_pdf_to_db(filepath)
    elif sub_choice == '3': return
    else: print("Invalid choice")

def load_pdf_to_db(filepath: str) -> None:
    """
    PURPOSE: Loads book metadata and text chunks with embeddings into a SQL Server database.\n
    ARGUMENTS: None\n
    RETURNS: None\n
    """
    pdf_details = pdf.get_pdf_details(filepath=rf"{filepath}")
    if not pdf_details: return
    
    try:
        conn = pyodbc.connect(get_database_connection_string())
        cursor = conn.cursor()
        for chunk, embedding in zip(pdf_details["CHUNKS"], pdf_details["EMBEDDED_CHUNKS"]):
            cursor.execute(
                """INSERT INTO BOOKS VALUES (?, ?, ?, ?, ?, CAST(? AS VARCHAR(MAX)))""", 
                (pdf_details["ISBN"], pdf_details["TITLE"], pdf_details["AUTHOR_FIRST_NAME"], pdf_details["AUTHOR_LAST_NAME"], chunk, str(embedding))
            )
            conn.commit()
        cursor.close()
        print("Data inserted successfully")
    except Exception as e: print("Data inserion failed", e)
    finally: conn.close()

def perform_vector_search_menu() -> None:
    """
    PURPOSE: Menu to perform a vector search based on user input question.\n
    ARGUMENTS: None\n
    RETURNS: None
    """
    print(ask_ai.ask_ollama(input("Enter your question: ")))

def perform_vector_search(question: str) -> tuple[str, List[str]]:
    """
    PURPOSE: Performs a vector search in the SQL Server database to find relevant text chunks based on a question.\n
    ARGUMENTS: question (str): The question to search for.\n
    RETURNS: tuple: The original question and a list of relevant text chunks.
    """
    try:
        query_embedding = str(ollama.embed(model="mxbai-embed-large", input=[question])['embeddings'][0])
        conn = pyodbc.connect(get_database_connection_string())
        cursor = conn.cursor()
        cursor.execute(
        """
        SELECT TOP 10 CHUNK
        FROM BOOKS
        ORDER BY VECTOR_DISTANCE('COSINE', EMBEDDED_CHUNK, CAST(CAST(? AS NVARCHAR(MAX)) AS VECTOR(1024))) ASC;
        """, (query_embedding,))
        rows = cursor.fetchall()
        cursor.close()
    except Exception as e: print("Query failed", e)
    finally: conn.close()
    return question, [row[0] for row in rows]
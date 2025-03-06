from dotenv import load_dotenv
import pyodbc
import os

class Database:
    def __init__(self):
        """
        PURPOSE: Initialize a database connector object\n
        ARGUMENT: None\n
        RETURN: None\n
        """
        load_dotenv()
        self.__driver = os.getenv("DATA_BASE_DRIVER")
        self.__server = os.getenv("DATA_BASE_SERVER")
        self.__database = os.getenv("DATA_BASE_DATABASE")
        self.__trusted_connection = os.getenv("TRUSTED_CONNECTION")
        self.__UID = os.getenv("UID")

    def execute_sql_statement(self, sql: str, arguments: set) -> None:
        """
        PURPOSE: Execute the SQL statement\n
        ARGUMENT: sql: the SQL statement to execute\n
        RETURN: None\n
        """
        try:
            connection = self.__get_database_connection()
            cursor = self.__get_database_cursor(connection=connection)
            return self.__get_sql_results(cursor=cursor, sql=sql, arguments=arguments)
        except Exception as e: print(e)
        finally: self.__close_database_connection(cursor=cursor, connection=connection)

    def __get_database_connection(self) -> pyodbc.Connection:
        """
        PURPOSE: Establish a connection to the database\n
        ARGUMENT: None\n
        RETURN: Database connection object\n
        """
        return pyodbc.connect(f"""
                            DRIVER={self.__driver};
                            SERVER={self.__server};
                            DATABASE={self.__database};
                            TRUSTED_CONNECTION={self.__trusted_connection};
                            UID={self.__UID};
                            """)

    def __get_database_cursor(self, connection: pyodbc.Connection) -> pyodbc.Cursor:
        """
        PURPOSE: Initialize a database cursor\n
        ARGUMENT: connection: The database connection object\n
        RETURN: A database cursor\n
        """
        return connection.cursor()

    def __get_sql_results(self, cursor: pyodbc.Cursor, sql: str, arguments: tuple) -> list[str]:
        """
        PURPOSE: Execute the SQL statement\n
        ARGUMENT: cursor: database cursor, sql: sql statement to execute\n
        RETURN: results of the sql statement being executed\n
        """
        return cursor.execute(f"EXEC {sql} {'?,' * len(arguments)}"[:-1], arguments).fetchall()

    def __close_database_connection(self, cursor: pyodbc.Cursor, connection: pyodbc.Connection) -> None:
        """
        PURPOSE: Close the connection to the database\n
        ARGUMENT: cursor: database cursor, connection: database connection object\n
        RETURN: None\n
        """
        cursor.close()
        connection.close()
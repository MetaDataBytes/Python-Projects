import db_func

def menu() -> None:
    """
    PURPOSE: Main menu to load PDFs to the database or ask questions.\n
    ARGUMENTS: None\n
    RETURNS: None
    """
    while True:
        print("1. Load PDF to Database")
        print("2. Ask a Question")
        print("3. Exit")
        choice = input("Enter your choice: ")
        print()
        if choice == '1': db_func.load_pdf_to_db_menu()
        elif choice == '2': db_func.perform_vector_search_menu()
        elif choice == '3': break
        else: print("Invalid choice")
        print()


if __name__ == "__main__": menu()
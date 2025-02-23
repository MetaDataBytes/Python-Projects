from dotenv import load_dotenv
from Supervisor_agent import get_supervisor_agent, print_introduction, print_response, print_goodbye
load_dotenv()


if __name__ == "__main__":
    app = get_supervisor_agent().compile()
    print_introduction()
    while True:
        prompt = input("User Prompt: ").strip().lower()
        if prompt == 'quit': break
        result = app.invoke({"messages": [{"role": "user", "content": prompt}]})
        print_response(result=result)
    print_goodbye()
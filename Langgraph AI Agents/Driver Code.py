from agents import get_supervisor_agent, print_results
from dotenv import load_dotenv
load_dotenv()


app = get_supervisor_agent().compile()
while True:
    print("Howdy!\n\nMy name is A.N.N.A, an AI assistant that can answer qustions and take action. What can I DO for you today?\nYou can respond with 'quit' to exit.", end='\n\n')
    prompt = input("User Prompt: ").strip().lower()
    if prompt == 'quit': break
    result = app.invoke({"messages": [{"role": "user", "content": prompt}]})
    print_results(result=result)
    print("\n\n\n")
print("Goodbye! --A.N.N.A.")
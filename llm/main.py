from openai import OpenAI
from loguru import logger
from model_selection import model_selection

def get_summarisation(message):
    template = """
    Autonomously summarize the following code:\n\n{messages}\n\nSummary:
    """
    user_message = f"user:{message}"
    system_message = f"system:{template}"

    feed = [
    {"role": "system", "content": system_message},
    {"role": "user", "content": user_message}
    ]
    
    response = model_selection(feed, "gpt")
    print(response)
    return response
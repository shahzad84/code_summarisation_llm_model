import os
import openai
from openai import OpenAI
from loguru import logger
from dotenv import load_dotenv
load_dotenv()
client=OpenAI(api_key=os.environ["OPENAI_API_KEY"])

def get_gpt(feed):
    try:
        chat_completion_resp=client.chat.completions.create(model="gpt-3.5-turbo", messages=feed,  max_tokens=600)
        response_message=chat_completion_resp.choices[0].message.content
        print(response_message)
        return response_message
    except openai.APIConnectionError as e:
        logger.error(F"Error communication with openai api: {e}")
        return "sorry, I am not able to generate response"

def model_selection(feed, model):
    if model == "gpt":
        response = get_gpt(feed)
        return response

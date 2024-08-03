from openai import OpenAI
import openai
from config import apikey


openai.api_key = apikey

response = openai.ChatCompletion.create(
    model="gpt-4o-mini-2024-07-18",
    prompt = "Write an email to my boss for resignation?",
    temperature=1,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
)


print(response)


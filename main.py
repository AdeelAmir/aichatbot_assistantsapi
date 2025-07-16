import openai
from dotenv import load_dotenv, find_dotenv

load_dotenv()
client = openai.OpenAI()
model = "gpt-4.1-nano"
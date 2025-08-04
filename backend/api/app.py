from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.chains.llm import LLMChain
from fastapi import FastAPI
import os
import uvicorn
from pydantic import BaseModel

load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

app = FastAPI()

# LLM
model = "gpt-4.1-nano"
llm = ChatOpenAI(model=model)  # use valid available model name

# Prompt + Output Parser
prompt = ChatPromptTemplate.from_template(
    "Write a poem on {title} for 1-3 years baby with 100 words"
)
output_parser = StrOutputParser()

# Chain
chain = LLMChain(prompt=prompt, llm=llm)

# Define request model
class PoemRequest(BaseModel):
    title: str

# Create routes
@app.post('/poem')
async def generate_poem(title: PoemRequest):
    response = chain.run({"title": title})
    return {'status': True, 'message': "Poem generated successfully", 'data': response}

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
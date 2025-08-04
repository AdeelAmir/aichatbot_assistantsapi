# import openai
from dotenv import load_dotenv
# from langchain_openai import ChatOpenAI
# from langchain_core.prompts import ChatPromptTemplate
# from langchain_core.output_parsers import StrOutputParser
#
# import streamlit as st
# import os
#
load_dotenv()
model = "gpt-4.1-nano"
#
# os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
# os.environ["LANGCHAIN_TRACING_V2"] = "true"
# os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
#
# prompt = ChatPromptTemplate.from_messages(
#     [
#         ("system", "You are a good assistant, Please response to the user queries"),
#         ("user", "Question: {question}")
#     ]
# )
#
# st.title("Langchain Demo with OPENAI API")
# input_text = st.text_input("Search the topic you want")
#
# llm = ChatOpenAI(model=model)
# output_parser = StrOutputParser()
# chain = prompt | llm | output_parser
#
# if input_text:
#     st.write(chain.invoke({'question': input_text}))

# from langchain_openai import ChatOpenAI
# from langchain_core.prompts import ChatPromptTemplate
# from langchain_core.output_parsers import StrOutputParser
#
# import streamlit as st
# import os
#
# os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
# os.environ["LANGCHAIN_TRACING_V2"] = "true"
# os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
#
# # Prompt
# prompt = ChatPromptTemplate.from_messages(
#     [
#         ("system", "You are a good assistant, please response to user queries"),
#         ("user", "Question: {question}")
#     ]
# )
#
# # streamlit
# st.title("Welcome to Langchain with OPENAI")
# input_text = st.text_input("Search for query")
#
# # model
# llm = ChatOpenAI(model=model)
# output_parser = StrOutputParser()
# chain = prompt | llm | output_parser
#
# if input_text:
#     st.write(chain.invoke({"question": input_text}))

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import os
import streamlit as st

os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')
os.environ['LANGCHAIN_TRACING_V2'] = "true"
os.environ['LANGCHAIN_API_KEY'] = os.getenv('LANGCHAIN_API_KEY')

# Prompt
prompt = ChatPromptTemplate(
    [
        ("system", "You are car showroom dealer assistant"),
        ("user", "Question: {question}")
    ]
)

# Get input from user
st.title("Welcome to Mercedes Benz Showroom, How may i help you?")
input_text = st.text_input('Search your query')

# Add search button
search_btn = st.button('Search')

# LLM
llm = ChatOpenAI(model=model)
# Output Parser
output_parser = StrOutputParser()
# Chain
chain = prompt | llm | output_parser

# Agent Response
if input_text and search_btn:
    with st.spinner('Thinking'):
        response = chain.invoke({'question': input_text})
        st.write(response)









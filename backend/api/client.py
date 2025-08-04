import streamlit as st
import requests
from pydantic import BaseModel

class PoemRequest(BaseModel):
    title: str

def generate_poem(input_text: PoemRequest):
    payload = {
        "title": input_text
    }
    response = requests.post('http://127.0.0.1:8000/poem', json=payload)

    if response.status_code == 200:
        result = response.json()
        return result.get("data", "No poem returned")
    else:
        return f"Error: {response.status_code} - An unhandled error exception"

st.title("Langchain 🦜 OPENAI Agent")
input_text = st.text_input("Enter poem title")

if input_text:
    response = generate_poem(input_text)
    st.write(response)
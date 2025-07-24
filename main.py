from fastapi import FastAPI, Depends, HTTPException
from chroma_connection import get_chroma_collection
from pydantic import BaseModel
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

app = FastAPI(title="School Learning App AI", version="1.0")

# Set the model to use
model = "gpt-4.1-nano"

class UploadBookRequest(BaseModel):
    book_id: int

class SearchBookRequest(BaseModel):
    book_id: int
    query: str

@app.post("/api/upload_book")
async def upload_book(request: UploadBookRequest, col = Depends(get_chroma_collection)):
    try:
        # load pdf file
        file_path = "rag/files/book1.pdf"  # Replace with actual file paths
        loader = PyPDFLoader(file_path=file_path)
        documents = loader.load()

        # Split the documents into chunks
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        documents = text_splitter.split_documents(documents)

        # add metadata to each document
        for doc in documents:
            doc.metadata = {"doc_id": str(request.book_id)}

        # Create embeddings
        embeddings = OpenAIEmbeddings()

        # Create a Chroma vector store
        Chroma.from_documents(documents, embeddings, collection_name="my_collection")

        return {"status": True, "message": "Book uploaded successfully"}
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.post("/api/search_book")
async def search_book(query: SearchBookRequest, col = Depends(get_chroma_collection)):
    try:
        # Rebuild vector store from collection
        
        embeddings = OpenAIEmbeddings()
        db = Chroma(
            embedding_function= embeddings,
            collection_name="my_collection",
        )

        # Create a retriever from the collection

        retriever = db.as_retriever(search_kwargs={
            "k": 3,
            "filter": {"doc_id": str(query.book_id)}
        })

        # Create a retrieval chain

        llm = ChatOpenAI(model_name=model)

        prompt = ChatPromptTemplate.from_template("""
        You are a helpful assistant. Answer the question based solely on the provided context.

        - Think step by step and provide a detailed, accurate answer.
        - If the context does not contain information relevant to the question, respond with: "Sorry, this is out of context."

        Context:
        {context}

        Question:
        {input}
        """)

        document_chain = create_stuff_documents_chain(llm, prompt=prompt)

        retrieval_chain = create_retrieval_chain(
            retriever,
            document_chain
        )

        result = retrieval_chain.invoke({"input": query.query})
    
        return {"status": True, "message": "Results retrieved successfully", "data": result["answer"]}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
from fastapi import FastAPI, Depends, HTTPException
from airag_chatbot.db.session import get_db, Base, engine
from airag_chatbot.db import models
from contextlib import asynccontextmanager
import uvicorn

# create table on startup
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup Logic
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    
    yield # App runs here

    # Optional: Shutdown logic Here


app = FastAPI(lifespan=lifespan)

@app.get("/")
async def read_root():
    return {"message": "Welcome to FastAPI on custom port!"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8005, reload=True)
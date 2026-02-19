from fastapi import FastAPI
from pydantic import BaseModel

from chatbot import ask


app = FastAPI(
    title="Chatbot PDF RAG Azure",
    version="1.0"
)


class Question(BaseModel):
    question: str


@app.get("/")
def root():
    return {"status": "online"}


@app.post("/ask")
def ask_question(data: Question):

    answer = ask(data.question)

    return {
        "question": data.question,
        "answer": answer
    }

from fastapi import FastAPI
from pydantic import BaseModel

from src.chatbot import ask


app = FastAPI(
    title="PDF RAG Chatbot API",
    version="1.0.0"
)


class QuestionRequest(BaseModel):
    question: str


class AnswerResponse(BaseModel):
    answer: str


@app.get("/")
def root():
    return {"status": "API running"}


@app.post("/ask", response_model=AnswerResponse)
def ask_question(request: QuestionRequest):

    answer = ask(request.question)

    return AnswerResponse(answer=answer)

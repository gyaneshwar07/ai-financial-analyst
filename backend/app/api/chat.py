from fastapi import APIRouter
from ..schemas import ChatRequest, ChatResponse
from ..agents.supervisor import run_finance_graph

router = APIRouter(prefix="/api", tags=["chat"])

@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    if not request.question.strip():
        return ChatResponse(answer="Please enter a question.")
    return ChatResponse(answer=run_finance_graph(request.question))

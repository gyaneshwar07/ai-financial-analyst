from fastapi import APIRouter, HTTPException
from ..schemas import ChatRequest, ChatResponse
from ..agents.supervisor import run_finance_graph

router = APIRouter(prefix="/api", tags=["chat"])


@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    if not request.question.strip():
        return ChatResponse(answer="Please enter a question.")

    try:
        answer = run_finance_graph(request.question)
        return ChatResponse(answer=answer)

    except Exception as e:
        error_message = str(e)

        # Gemini quota / rate limit
        if "RESOURCE_EXHAUSTED" in error_message or "429" in error_message:
            raise HTTPException(
                status_code=429,
                detail="Gemini API quota exhausted. Please try again later."
            )

        # Other unexpected backend errors
        raise HTTPException(
            status_code=500,
            detail=f"Backend error: {error_message}"
        )
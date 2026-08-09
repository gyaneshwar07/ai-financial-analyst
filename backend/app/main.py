from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .api.chat import router as chat_router
from .api.documents import router as document_router

app = FastAPI(title="AI Financial Analyst API", version="1.0.0")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], allow_credentials=True,
    allow_methods=["*"], allow_headers=["*"],
)
app.include_router(chat_router)
app.include_router(document_router)

@app.get("/")
def home():
    return {"message": "AI Financial Analyst API is running."}

@app.get("/health")
def health():
    return {"status": "healthy"}

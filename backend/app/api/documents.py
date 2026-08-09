from pathlib import Path
from fastapi import APIRouter, File, UploadFile, HTTPException
from ..schemas import UploadResponse
from ..rag.ingest import create_vector_store

router = APIRouter(prefix="/api", tags=["documents"])
UPLOAD_PATH = Path("data/uploads")
UPLOAD_PATH.mkdir(parents=True, exist_ok=True)

@router.post("/upload", response_model=UploadResponse)
async def upload_document(file: UploadFile = File(...)):
    if not file.filename or not file.filename.lower().endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are supported.")
    file_path = UPLOAD_PATH / Path(file.filename).name
    content = await file.read()
    file_path.write_bytes(content)
    try:
        result = create_vector_store(str(file_path))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return UploadResponse(message="PDF processed successfully.", **result)

from pathlib import Path

from pypdf import PdfReader
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings


INDEX_PATH = Path("data/faiss_index")


def create_vector_store(file_path: str):
    reader = PdfReader(file_path)

    documents = []

    for page_number, page in enumerate(reader.pages):
        text = page.extract_text() or ""

        if text.strip():
            documents.append(
                Document(
                    page_content=text,
                    metadata={
                        "source": Path(file_path).name,
                        "page": page_number + 1,
                    },
                )
            )

    if not documents:
        raise ValueError("No readable text was found in the PDF.")

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=150,
    )

    chunks = splitter.split_documents(documents)

    # Local Hugging Face embeddings
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    store = FAISS.from_documents(chunks, embeddings)

    INDEX_PATH.mkdir(parents=True, exist_ok=True)
    store.save_local(str(INDEX_PATH))

    return {
        "pages": len(documents),
        "chunks": len(chunks),
        "file": Path(file_path).name,
    }

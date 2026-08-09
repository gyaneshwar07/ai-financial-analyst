from pathlib import Path

from langchain_core.tools import tool
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings


INDEX_PATH = Path("data/faiss_index")


def get_vector_store():
    if not (INDEX_PATH / "index.faiss").exists():
        return None

    # Use the SAME local embedding model used during PDF indexing
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    return FAISS.load_local(
        str(INDEX_PATH),
        embeddings,
        allow_dangerous_deserialization=True,
    )


@tool
def search_financial_documents(query: str) -> str:
    """Search uploaded financial PDFs and return relevant passages with source metadata."""

    store = get_vector_store()

    if store is None:
        return "No financial documents have been uploaded yet."

    docs = store.similarity_search(query, k=4)

    if not docs:
        return "No relevant information was found."

    return "\n\n---\n\n".join(
        f"Source: {d.metadata.get('source', 'unknown')}, "
        f"page {d.metadata.get('page', '')}\n"
        f"Content: {d.page_content}"
        for d in docs
    )

import requests
import streamlit as st
import os
BACKEND_URL = os.getenv("BACKEND_URL", "http://127.0.0.1:8000")

st.set_page_config(page_title="AI Financial Analyst", page_icon="💰", layout="wide")
st.title("💰 AI Financial Analyst")
st.caption("GenAI + LangGraph + Tool Calling + RAG")

with st.sidebar:
    st.header("📄 Financial Documents")
    uploaded_file = st.file_uploader("Upload an annual report or financial PDF", type=["pdf"])
    if uploaded_file is not None and st.button("Process PDF"):
        with st.spinner("Reading, chunking and indexing PDF..."):
            try:
                r = requests.post(
                    f"{BACKEND_URL}/api/upload",
                    files={"file": (uploaded_file.name, uploaded_file.getvalue(), "application/pdf")},
                    timeout=180,
                )
                if r.ok:
                    d = r.json()
                    st.success(f"Processed {d['file']}: {d['pages']} pages, {d['chunks']} chunks.")
                else:
                    st.error(r.text)
            except requests.RequestException as e:
                st.error(f"Backend connection failed: {e}")

chat_tab, stock_tab, about_tab = st.tabs(["🤖 AI Analyst", "📊 Stock Analysis", "ℹ️ About"])

with chat_tab:
    st.subheader("Ask the AI Financial Analyst")
    if "messages" not in st.session_state:
        st.session_state.messages = []
    for m in st.session_state.messages:
        with st.chat_message(m["role"]):
            st.markdown(m["content"])
    question = st.chat_input("Example: Analyze TCS fundamentals")
    if question:
        st.session_state.messages.append({"role": "user", "content": question})
        with st.chat_message("user"):
            st.markdown(question)
        with st.chat_message("assistant"):
            with st.spinner("Thinking and using tools when needed..."):
                try:
                    r = requests.post(
                        f"{BACKEND_URL}/api/chat",
                        json={"question": question},
                        timeout=180,
                    )
                    answer = r.json()["answer"] if r.ok else f"Backend error: {r.text}"
                except requests.RequestException as e:
                    answer = f"Could not connect to FastAPI: {e}"
            st.markdown(answer)
        st.session_state.messages.append({"role": "assistant", "content": answer})

with stock_tab:
    st.subheader("Quick Stock Analysis")
    symbol = st.text_input("Stock symbol", "TCS.NS")
    if st.button("Analyze Stock"):
        q = f"Get the latest price and basic financial information for {symbol}."
        with st.spinner("Calling financial tools..."):
            try:
                r = requests.post(f"{BACKEND_URL}/api/chat", json={"question": q}, timeout=180)
                if r.ok:
                    st.markdown(r.json()["answer"])
                else:
                    st.error(r.text)
            except requests.RequestException as e:
                st.error(str(e))

with about_tab:
    st.subheader("Project Architecture")
    st.code("""Streamlit\n   ↓\nFastAPI\n   ↓\nLangGraph\n   ↓\nGemini + Tool Calling\n   ↓\nFinance Tools / RAG\n   ↓\nFinal Answer""")
    st.markdown("""
    **Current modules:** stock price tool, company fundamentals tool, growth calculator,
    PDF RAG with FAISS, Gemini tool calling, and a LangGraph agent loop.

    ⚠️ Educational/research use only. This is not personalized financial advice.
    """)

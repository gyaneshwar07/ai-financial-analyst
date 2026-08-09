# 💰 AI Financial Analyst

An AI-powered financial analysis assistant that combines **Generative AI, LangGraph, LangChain, RAG, FAISS, and financial tools** to analyze financial documents and answer stock-related questions.

The application allows users to upload financial PDFs such as annual reports and ask questions about revenue, profit, business segments, financial performance, and other company information.

It can also handle stock-related queries using financial tools and current market data.

---

## 🚀 Features

### 📄 Financial Document Analysis
- Upload financial PDFs / annual reports
- Extract text from PDF documents
- Split documents into smaller chunks
- Generate local embeddings
- Store embeddings in FAISS
- Retrieve relevant financial information using semantic search
- Answer questions using retrieved document context

### 📈 Stock Analysis
- Query current stock information
- Analyze stock fundamentals
- Retrieve financial metrics
- Answer stock-related questions using financial tools

### 🤖 AI Agent

The application uses **LangGraph** to orchestrate the financial analysis workflow.

The agent can decide which capability is required for a query:

- Financial document retrieval
- Financial/stock tools
- LLM-based reasoning
- Final response generation

### 🔍 RAG Pipeline

The application implements Retrieval-Augmented Generation:

```text
PDF
 ↓
Text Extraction
 ↓
Text Chunking
 ↓
Hugging Face Embeddings
 ↓
FAISS Vector Store
 ↓
Similarity Search
 ↓
Relevant Context
 ↓
Gemini LLM
 ↓
Final Answer

## Setup

### 1. Create a virtual environment

```bash
python -m venv venv
venv\\Scripts\\activate
```

### 2. Install packages

```bash
pip install -r backend/requirements.txt
pip install -r frontend/requirements.txt
```

### 3. Create `.env`

Copy `.env.example` to `.env` and add your Gemini API key:

```env
GOOGLE_API_KEY=your_key_here
```

### 4. Run backend

From the project root:

```bash
uvicorn backend.app.main:app --reload
```

### 5. Run Streamlit in another terminal

```bash
streamlit run frontend/streamlit_app.py
```

## Test questions

Start with these:

1. `What is the latest price of TCS?`
2. `Give me the basic financials of RELIANCE.`
3. `Calculate the growth from 100 to 125.`
4. Upload an annual report, then ask: `What are the major risks mentioned in this report?`
5. `Analyze TCS fundamentals using current data.`

## Important

Market data may be delayed/incomplete. The application is for educational and research purposes and does not provide personalized investment advice.

🔮 Future Improvements
Add more financial data APIs, 
Add multi-agent financial research,
Add financial charts and visualizations,
Add portfolio analysis,
Add company comparison,
Add historical stock analysis,
Add citation links to annual report pages,
Add conversation memory,
Add authentication,
Deploy the application publicly, and
Add automated evaluation for RAG responses

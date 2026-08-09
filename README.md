# AI Financial Analyst — Full Stack GenAI + Agentic AI

This is a beginner-friendly finance AI project built in the same style as a simple LangChain/LangGraph tool-calling application.

## Stack

- Python
- FastAPI
- Streamlit
- LangChain
- LangGraph
- Gemini 2.5 Flash
- Gemini embeddings
- FAISS
- yfinance
- PyPDF

## Flow

```text
Streamlit
   ↓
FastAPI
   ↓
LangGraph
   ↓
Gemini
   ↓
Tool Calling
   ├── get_stock_price
   ├── get_company_financials
   ├── calculate_growth
   └── search_financial_documents
```

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

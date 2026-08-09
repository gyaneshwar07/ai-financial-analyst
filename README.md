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
=======
An AI-powered financial analysis assistant built with **LangGraph, LangChain, Gemini, RAG, FAISS, FastAPI, and Streamlit**.

The application can analyze uploaded financial reports, retrieve relevant financial information using semantic search, and answer stock-related questions using financial tools and current market data.

## 🚀 Features

### 📄 Financial Document Analysis

* Upload financial PDFs and annual reports
* Extract text from PDF documents
* Split documents into smaller chunks
* Generate local embeddings using Hugging Face
* Store embeddings in FAISS
* Retrieve relevant information using semantic search
* Generate answers using retrieved document context

### 📈 Stock Analysis

* Retrieve latest available stock information
* Analyze stock fundamentals
* Retrieve financial metrics
* Use tool calling for financial data

### 🤖 Agentic AI

The application uses **LangGraph** to orchestrate the AI workflow.

Depending on the user's query, the system can use:

* Financial document RAG
* Stock/financial tools
* LLM reasoning
* Multiple steps of agent execution

### 🧠 Local Embeddings

The project uses:

```text
sentence-transformers/all-MiniLM-L6-v2
```

for document embeddings.

Embeddings are generated locally instead of using the Gemini embedding API, reducing dependency on external embedding API quotas.

---

# 🏗️ Architecture

```text
                    User
                      │
                      ▼
              Streamlit Frontend
                      │
                      │ REST API
                      ▼
                FastAPI Backend
                      │
                      ▼
              LangGraph Supervisor
                      │
             ┌────────┴────────┐
             │                 │
             ▼                 ▼
       Financial Tools       RAG Tool
             │                 │
             ▼                 ▼
       Market Data         FAISS Vector DB
                               │
                               ▼
                    Hugging Face Embeddings
                               │
                               ▼
                        Financial PDFs
                               │
             ┌─────────────────┘
             ▼
          Gemini LLM
             │
             ▼
        Final Response
```

---

# 🛠️ Tech Stack

| Technology            | Purpose                  |
| --------------------- | ------------------------ |
| Python                | Core development         |
| LangChain             | LLM and tool integration |
| LangGraph             | Agent orchestration      |
| Gemini                | Large Language Model     |
| Hugging Face          | Local embeddings         |
| Sentence Transformers | Text embeddings          |
| FAISS                 | Vector database          |
| PyPDF                 | PDF processing           |
| FastAPI               | REST API backend         |
| Uvicorn               | ASGI server              |
| Streamlit             | Frontend                 |
| python-dotenv         | Environment variables    |

---

# 📂 Project Structure

```text
ai-financial-analyst/
│
├── backend/
│   ├── app/
│   │   ├── agents/
│   │   ├── api/
│   │   ├── rag/
│   │   ├── tools/
│   │   ├── config.py
│   │   ├── llm.py
│   │   ├── main.py
│   │   ├── schemas.py
│   │   └── state.py
│   │
│   └── requirements.txt
│
├── frontend/
│   ├── streamlit_app.py
│   └── requirements.txt
│
├── data/
│   └── uploads/
│
├── .gitignore
├── README.md
└── .env
```

> `.env`, uploaded documents, FAISS indexes, and virtual environments are excluded from Git using `.gitignore`.

---

# 🔄 How It Works

## 1. User Uploads a Financial PDF

The user uploads an annual report or other financial document through the Streamlit frontend.

## 2. PDF Processing

The FastAPI backend receives the document and extracts its text using PyPDF.

## 3. Text Chunking

The extracted text is divided into smaller overlapping chunks using a text splitter.

This allows the retrieval system to find more relevant sections of large financial reports.

## 4. Embedding Generation

Each document chunk is converted into a numerical vector using:

```text
sentence-transformers/all-MiniLM-L6-v2
```

## 5. FAISS Storage

The vectors are stored in a FAISS index for efficient similarity search.

## 6. User Asks a Question

For example:

```text
What was the company's total income in FY2025-26?
```

## 7. LangGraph Agent

LangGraph manages the agent workflow and determines which capability is required.

For a financial-document question:

```text
User Question
     ↓
LangGraph
     ↓
RAG Tool
     ↓
FAISS Similarity Search
     ↓
Relevant Document Chunks
     ↓
Gemini
     ↓
Final Answer
```

For a stock question:

```text
User Question
     ↓
LangGraph
     ↓
Financial Tool
     ↓
Market Data
     ↓
Gemini
     ↓
Final Answer
```

---

# 🧠 Why LangGraph?

LangGraph is used to manage the agent workflow as a graph of states and nodes.

It provides control over:

* Agent state
* Tool calling
* Conditional routing
* Multi-step workflows
* Extensibility
* Agent execution

This makes the application more flexible than a simple LLM chatbot.

---

# 🔧 Example Queries

### 📄 Financial Document Analysis

```text
What was the company's total income in FY2025-26?
```

```text
What was the percentage growth in total income?
```

```text
What were the company's major business segments?
```

```text
Compare FY2024-25 and FY2025-26 financial performance.
```

```text
What are the major risks mentioned in the annual report?
```

### 📈 Stock Analysis

```text
What is the latest available price of TCS?
```

```text
Give me the latest financial data for RELIANCE.
```

```text
Analyze TCS fundamentals.
```

```text
What is TCS's P/E ratio?
```

```text
What is the market capitalization of TCS?
```

### 🤖 Agentic Analysis

```text
Analyze TCS using current market data.
```

```text
Analyze the uploaded annual report and summarize the company's financial performance.
```

```text
Compare the company's financial performance with its current stock information.
```

---

# ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/gyaneshwar07/ai-financial-analyst.git
```

Navigate to the project:

```bash
cd ai-financial-analyst
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it on Windows:

```powershell
venv\Scripts\activate
```

Install backend dependencies:

```bash
pip install -r backend/requirements.txt
```

Install frontend dependencies:

```bash
pip install -r frontend/requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file in the project root:

```env
GOOGLE_API_KEY=your_google_api_key
```

Never commit your actual API key to GitHub.

---

# ▶️ Run the Application

Start the FastAPI backend:

```bash
uvicorn backend.app.main:app --reload
```

Open another terminal and start Streamlit:

```bash
streamlit run frontend/streamlit_app.py
```

The FastAPI API will be available locally at:

```text
http://127.0.0.1:8000
```

FastAPI Swagger documentation:

```text
http://127.0.0.1:8000/docs
```

Market data may be delayed/incomplete. The application is for educational and research purposes and does not provide personalized investment advice.

# 🔐 Security

The project excludes sensitive and generated files from Git:

```text
.env
venv/
.venv/
__pycache__/
*.pyc
data/uploads/
data/faiss_index/
.streamlit/
```

API keys should always be stored using environment variables or deployment secrets.

---

# 🚀 Future Improvements

* Deploy the complete application publicly
* Add portfolio analysis
* Add company comparison
* Add historical stock analysis
* Add financial charts
* Add source citations for retrieved PDF information
* Add conversation memory
* Add authentication
* Add more financial APIs
* Add automated RAG evaluation
* Add specialized financial research agents

---

# ⚠️ Disclaimer

This project is intended for **educational and demonstration purposes only**.

Market data may be delayed or incomplete. The application does not provide personalized investment advice.

---

# 👨‍💻 Author

**Gyaneshwar Kumar**

GitHub:
https://github.com/gyaneshwar07

LinkedIn:
https://www.linkedin.com/in/gyaneshwar-kumar-7744472a3/

---

⭐ If you found this project useful, consider giving the repository a star

from langchain_core.messages import SystemMessage
from langgraph.prebuilt import ToolNode
from ..llm import llm
from ..state import FinanceState
from ..tools.finance_tools import finance_tools
from ..tools.rag_tools import search_financial_documents

all_tools = finance_tools + [search_financial_documents]
finance_llm = llm.bind_tools(all_tools)

SYSTEM_PROMPT = """
You are an AI Financial Analyst.

Use tools whenever the question requires current market data, company fundamentals,
financial calculations, or information from an uploaded financial document.
Never invent financial numbers. Explain important calculations. Clearly distinguish
facts from interpretation. If data is unavailable, say so. Do not give personalized
buy/sell instructions or claim certainty. This is educational financial research.
"""

def finance_agent(state: FinanceState):
    messages = [SystemMessage(content=SYSTEM_PROMPT), *state["messages"]]
    response = finance_llm.invoke(messages)
    return {"messages": [response], "agent": "finance_agent"}

tool_node = ToolNode(all_tools)

from typing import Literal
from langchain_core.messages import HumanMessage, AIMessage
from langgraph.graph import StateGraph, START, END
from .finance_agent import finance_agent, tool_node
from ..state import FinanceState

def route_after_agent(state: FinanceState) -> Literal["tools", "end"]:
    last = state["messages"][-1]
    if getattr(last, "tool_calls", None):
        return "tools"
    return "end"

def build_graph():
    graph = StateGraph(FinanceState)
    graph.add_node("finance_agent", finance_agent)
    graph.add_node("tools", tool_node)
    graph.add_edge(START, "finance_agent")
    graph.add_conditional_edges(
        "finance_agent", route_after_agent,
        {"tools": "tools", "end": END},
    )
    graph.add_edge("tools", "finance_agent")
    return graph.compile()

finance_graph = build_graph()

def run_finance_graph(question: str) -> str:
    result = finance_graph.invoke(
        {
            "messages": [HumanMessage(content=question)],
            "question": question,
            "agent": "",
        }
    )

    messages = result["messages"]

    # Check messages from the end
    for message in reversed(messages):

        # We only want the AI's final answer
        if isinstance(message, AIMessage):

            content = message.content

            # Case 1: normal string response
            if isinstance(content, str):
                if content.strip():
                    return content

            # Case 2: Gemini structured content
            if isinstance(content, list):

                text_parts = []

                for item in content:

                    if isinstance(item, dict):

                        if item.get("type") == "text":
                            text_parts.append(
                                item.get("text", "")
                            )

                        elif "text" in item:
                            text_parts.append(
                                item["text"]
                            )

                final_text = "".join(text_parts).strip()

                if final_text:
                    return final_text

    return "I could not generate an answer."

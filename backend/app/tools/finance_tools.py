from langchain_core.tools import tool
import yfinance as yf

def clean_symbol(symbol: str) -> str:
    symbol = symbol.strip().upper()
    mapping = {
        "TCS": "TCS.NS", "RELIANCE": "RELIANCE.NS",
        "INFY": "INFY.NS", "HDFCBANK": "HDFCBANK.NS",
        "ICICIBANK": "ICICIBANK.NS", "SBIN": "SBIN.NS",
    }
    return mapping.get(symbol, symbol)

@tool
def get_stock_price(symbol: str) -> dict:
    """Get the latest available stock price and recent OHLCV data."""
    symbol = clean_symbol(symbol)
    history = yf.Ticker(symbol).history(period="5d")
    if history.empty:
        return {"error": f"No market data found for {symbol}"}
    last = history.iloc[-1]
    return {
        "symbol": symbol,
        "date": str(history.index[-1].date()),
        "open": round(float(last["Open"]), 2),
        "high": round(float(last["High"]), 2),
        "low": round(float(last["Low"]), 2),
        "close": round(float(last["Close"]), 2),
        "volume": int(last["Volume"]),
    }

@tool
def get_company_financials(symbol: str) -> dict:
    """Get basic company fundamentals from Yahoo Finance."""
    symbol = clean_symbol(symbol)
    info = yf.Ticker(symbol).info
    return {
        "symbol": symbol,
        "company_name": info.get("longName", symbol),
        "sector": info.get("sector"),
        "industry": info.get("industry"),
        "market_cap": info.get("marketCap"),
        "pe_ratio": info.get("trailingPE"),
        "eps": info.get("trailingEps"),
        "roe": info.get("returnOnEquity"),
        "debt_to_equity": info.get("debtToEquity"),
        "profit_margin": info.get("profitMargins"),
        "revenue": info.get("totalRevenue"),
    }

@tool
def calculate_growth(old_value: float, new_value: float) -> float:
    """Calculate percentage growth between two values."""
    if old_value == 0:
        return 0.0
    return round(((new_value - old_value) / abs(old_value)) * 100, 2)

finance_tools = [get_stock_price, get_company_financials, calculate_growth]

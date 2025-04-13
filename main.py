from mcp.server.fastmcp import FastMCP
import yfinance as yf

mcp = FastMCP("Stocks MCP")

@mcp.tool()
def get_stock_price(ticker: str, period: str = "1mo", interval: str = "1d"):
    """
    Fetch historical stock price data.

    Parameters:
        ticker (str): Stock ticker. Do not use the company name, use ticker.
        period (str): Time period to fetch (e.g., "1d", "5d", "1mo", "3mo", "6mo", "1y", "5y", "max").
        
    Returns:
        DataFrame: Historical stock price data.
    """
    try:
        stock = yf.Ticker(ticker)
        hist = stock.history(period=period, interval=interval)
        if hist.empty:
            print("No data returned. Check the ticker and timeframe.")
        return hist
    except Exception as e:
        print(f"Error fetching data: {e}")
        return None

if __name__ == "__main__":
    mcp.run(transport='stdio')

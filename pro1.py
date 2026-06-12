from mcp.server.fastmcp import FastMCP

mcp = FastMCP("CheckEvenOdd")

@mcp.tool()
def check_even_odd(number: int) -> str:
    """Check whether a given number is Even or Odd."""
    if number % 2 == 0:
        return f"{number} is Even"
    return f"{number} is Odd"

if __name__ == "__main__":
    mcp.run()
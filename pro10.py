from mcp.server.fastmcp import FastMCP

mcp = FastMCP("SumOfDigits")

@mcp.tool()
def sum_of_digits(number: int) -> dict:
    """Calculate the sum of digits of a given number."""
    n = abs(number)
    total = sum(int(d) for d in str(n))
    return {"number": number, "sum_of_digits": total}

if __name__ == "__main__":
    mcp.run()
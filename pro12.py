from mcp.server.fastmcp import FastMCP

mcp = FastMCP("FactorsOfNumber")

@mcp.tool()
def factors_of_number(number: int) -> dict:
    """Find all factors of a given positive integer."""
    if number <= 0:
        return {"error": "Number must be a positive integer"}
    factors = [i for i in range(1, number + 1) if number % i == 0]
    return {"number": number, "factors": factors}

if __name__ == "__main__":
    mcp.run()
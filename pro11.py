from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Factorial")

@mcp.tool()
def factorial(number: int) -> dict:
    """Calculate the factorial of a non-negative integer."""
    if number < 0:
        return {"error": "Factorial is not defined for negative numbers"}
    result = 1
    for i in range(2, number + 1):
        result *= i
    return {"number": number, "factorial": result}

if __name__ == "__main__":
    mcp.run()
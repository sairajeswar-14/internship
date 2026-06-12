from mcp.server.fastmcp import FastMCP

mcp = FastMCP("ArithmeticOperations")

@mcp.tool()
def arithmetic_operations(a: float, b: float) -> dict:
    """Perform addition, subtraction, multiplication, and division on two numbers."""
    result = {
        "addition": a + b,
        "subtraction": a - b,
        "multiplication": a * b,
    }
    if b != 0:
        result["division"] = a / b
    else:
        result["division"] = "undefined (division by zero)"
    return result

if __name__ == "__main__":
    mcp.run()
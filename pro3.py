from mcp.server.fastmcp import FastMCP

mcp = FastMCP("GreatestOfTwo")

@mcp.tool()
def greatest_of_two(a: float, b: float) -> str:
    """Find the greatest of two numbers."""
    if a == b:
        return f"Both numbers are equal: {a}"
    greater = a if a > b else b
    return f"The greatest number is {greater}"

if __name__ == "__main__":
    mcp.run()
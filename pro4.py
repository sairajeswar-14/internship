from mcp.server.fastmcp import FastMCP

mcp = FastMCP("SignOfNumber")

@mcp.tool()
def sign_of_number(number: float) -> str:
    """Determine whether a number is Positive, Negative, or Zero."""
    if number > 0:
        return f"{number} is Positive"
    elif number < 0:
        return f"{number} is Negative"
    return f"{number} is Zero"

if __name__ == "__main__":
    mcp.run()
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("MultiplicationTable")

@mcp.tool()
def multiplication_table(number: int, upto: int = 10) -> list[str]:
    """Generate the multiplication table of a given number (default up to 10)."""
    return [f"{number} x {i} = {number * i}" for i in range(1, upto + 1)]

if __name__ == "__main__":
    mcp.run()
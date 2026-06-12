from mcp.server.fastmcp import FastMCP

mcp = FastMCP("MultiplicationTableOf9")

@mcp.tool()
def multiplication_table_of_9() -> list[str]:
    """Generate the multiplication table of 9 (1 to 10)."""
    return [f"9 x {i} = {9 * i}" for i in range(1, 11)]

if __name__ == "__main__":
    mcp.run()
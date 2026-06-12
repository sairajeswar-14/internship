from mcp.server.fastmcp import FastMCP

mcp = FastMCP("First10NaturalNumbers")

@mcp.tool()
def first_10_natural_numbers() -> list[int]:
    """Return the first 10 natural numbers (1 to 10)."""
    return list(range(1, 11))

if __name__ == "__main__":
    mcp.run()
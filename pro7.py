from mcp.server.fastmcp import FastMCP

mcp = FastMCP("FirstNNaturalNumbers")

@mcp.tool()
def first_n_natural_numbers(n: int) -> list[int]:
    """Return the first n natural numbers (1 to n)."""
    if n < 1:
        return []
    return list(range(1, n + 1))

if __name__ == "__main__":
    mcp.run()
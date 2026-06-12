from mcp.server.fastmcp import FastMCP

mcp = FastMCP("SumOfList")

@mcp.tool()
def sum_of_list(numbers: list[float]) -> dict:
    """Calculate the sum of all elements in a list of numbers."""
    return {"numbers": numbers, "sum": sum(numbers)}

if __name__ == "__main__":
    mcp.run()
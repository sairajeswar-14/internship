from mcp.server.fastmcp import FastMCP

mcp = FastMCP("PrimeCheck")

@mcp.tool()
def is_prime(number: int) -> str:
    """Check whether a given number is a Prime number."""
    if number < 2:
        return f"{number} is not Prime"
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return f"{number} is not Prime"
    return f"{number} is Prime"

if __name__ == "__main__":
    mcp.run()
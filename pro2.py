from mcp.server.fastmcp import FastMCP

mcp = FastMCP("CheckVotingEligibility")

@mcp.tool()
def check_voting_eligibility(age: int) -> str:
    """Check whether a person is eligible to vote (age >= 18)."""
    if age >= 18:
        return f"Age {age}: Eligible to vote"
    return f"Age {age}: Not eligible to vote"

if __name__ == "__main__":
    mcp.run()
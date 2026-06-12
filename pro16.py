import io
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("ReadCsvPandas")

@mcp.tool()
def read_csv_data(csv_text: str) -> dict:
    """
    Read CSV data (as raw text) using pandas and return basic info:
    columns, number of rows, and the first 5 rows as records.

    Pass CSV content as plain text, e.g.: "name,age\\nAlice,30\\nBob,25"
    """
    import pandas as pd

    df = pd.read_csv(io.StringIO(csv_text))
    return {
        "columns": list(df.columns),
        "row_count": len(df),
        "preview": df.head(5).to_dict(orient="records"),
    }

if __name__ == "__main__":
    mcp.run()
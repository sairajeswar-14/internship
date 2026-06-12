from mcp.server.fastmcp import FastMCP

mcp = FastMCP("StudentGrade")

@mcp.tool()
def student_grade(marks: float) -> str:
    """Calculate a student's grade based on marks (0-100).

    Grading scale:
        >= 90 : A
        >= 75 : B
        >= 60 : C
        >= 40 : D
        <  40 : F (Fail)
    """
    if marks >= 90:
        grade = "A"
    elif marks >= 75:
        grade = "B"
    elif marks >= 60:
        grade = "C"
    elif marks >= 40:
        grade = "D"
    else:
        grade = "F (Fail)"
    return f"Marks: {marks} -> Grade: {grade}"

if __name__ == "__main__":
    mcp.run()
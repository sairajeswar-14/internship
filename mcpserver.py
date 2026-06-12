from fastmcp import FastMCP
import pandas as pd

mcp = FastMCP("MyPythonTools")


@mcp.tool()
def even_or_odd(num: int) -> str:
    if num % 2 == 0:
        return "Even"
    return "Odd"


@mcp.tool()
def voting_eligibility(age: int) -> str:
    if 18 <= age <= 100:
        return "Eligible for vote"
    return "Not eligible for vote"


@mcp.tool()
def compare_numbers(x: int, y: int) -> str:
    if x == y:
        return "Both are equal"
    elif x < y:
        return "Y is greater"


@mcp.tool()
def check_number(num: int) -> str:
    if num > 0:
        return "Positive number"
    elif num == 0:
        return "Zero"
    return "Negative number"


@mcp.tool()
def calculator(x: int, y: int) -> dict:
    return {
        "addition": x + y,
        "subtraction": x - y,
        "multiplication": x * y,
        "division": x // y
    }


@mcp.tool()
def first_10_numbers() -> list:
    return [i for i in range(1, 11)]


@mcp.tool()
def numbers_upto_n(n: int) -> list:
    return [i for i in range(1, n + 1)]


@mcp.tool()
def multiplication_table(num: int) -> list:
    return [f"{num} x {i} = {num * i}" for i in range(1, 11)]


@mcp.tool()
def table_of_9() -> list:
    return [f"9 x {i} = {9 * i}" for i in range(1, 11)]


@mcp.tool()
def sum_of_digits(num: int) -> int:
    total = 0
    while num > 0:
        digit = num % 10
        total += digit
        num = num // 10
    return total


@mcp.tool()
def factorial(num: int) -> int:
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    return fact


@mcp.tool()
def factors(num: int) -> list:
    return [i for i in range(1, num + 1) if num % i == 0]


@mcp.tool()
def prime_check(num: int) -> str:
    count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            count += 1

    if count == 2:
        return "Prime"
    return "Not Prime"


@mcp.tool()
def sum_of_list(numbers: list[int]) -> int:
    return sum(numbers)


@mcp.tool()
def student_grade(name: str, maths: int, physics: int, chemistry: int) -> dict:
    total = maths + physics + chemistry

    if total >= 270:
        grade = "A"
    elif total >= 240:
        grade = "B"
    elif total >= 180:
        grade = "C"
    else:
        grade = "Fail"

    return {
        "name": name,
        "total": total,
        "grade": grade
    }


@mcp.tool()
def student_csv_data() -> list:
    data = {
        "Name": ["Ram", "Sam", "Ravi"],
        "Age": [20, 21, 19],
        "Marks": [90, 85, 95]
    }

    df = pd.DataFrame(data)
    df.to_csv("students.csv", index=False)

    return df.head(10).to_dict(orient="records")


if __name__ == "__main__":
    mcp.run()
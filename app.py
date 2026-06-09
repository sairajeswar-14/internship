import streamlit as st
import pandas as pd

st.title("Python Programs in Streamlit")

option = st.selectbox(
    "Select Experiment",
    [
        "1. Check Even or Odd",
        "2. Check Voting Eligibility",
        "3. Greatest of Two Numbers",
        "4. Sign of a Number",
        "5. Arithmetic Operations",
        "6. First 10 Natural Numbers",
        "7. First n Natural Numbers",
        "8. Multiplication Table (Given Number)",
        "9. Multiplication Table of 9",
        "10. Sum of Digits",
        "11. Factorial of a Number",
        "12. Factors of a Number",
        "13. Prime Number Check",
        "14. Sum of Elements in a List",
        "15. Student Grade Calculation",
        "16. Read CSV Using Pandas"
    ]
)


if option == "1. Check Even or Odd":
    num = st.number_input("Enter a number", step=1)

    if st.button("Check"):
        if num % 2 == 0:
            st.success("Even Number")
        else:
            st.success("Odd Number")


elif option == "2. Check Voting Eligibility":
    age = st.number_input("Enter age", step=1)

    if st.button("Check Eligibility"):
        if age >= 18:
            st.success("Eligible to Vote")
        else:
            st.error("Not Eligible")


elif option == "3. Greatest of Two Numbers":
    a = st.number_input("Enter first number")
    b = st.number_input("Enter second number")

    if st.button("Find Greatest"):
        if a > b:
            st.success(f"{a} is greater")
        elif b > a:
            st.success(f"{b} is greater")
        else:
            st.success("Both are equal")


elif option == "4. Sign of a Number":
    num = st.number_input("Enter number")

    if st.button("Check Sign"):
        if num > 0:
            st.success("Positive Number")
        elif num < 0:
            st.success("Negative Number")
        else:
            st.success("Zero")


elif option == "5. Arithmetic Operations":
    a = st.number_input("Enter first number")
    b = st.number_input("Enter second number")

    if st.button("Calculate"):
        st.write("Addition:", a + b)
        st.write("Subtraction:", a - b)
        st.write("Multiplication:", a * b)

        if b != 0:
            st.write("Division:", a / b)
        else:
            st.error("Division by zero not possible")


elif option == "6. First 10 Natural Numbers":
    if st.button("Show Numbers"):
        for i in range(1, 11):
            st.write(i)


elif option == "7. First n Natural Numbers":
    n = st.number_input("Enter n", step=1)

    if st.button("Display"):
        i = 1
        while i <= n:
            st.write(i)
            i += 1


elif option == "8. Multiplication Table (Given Number)":
    num = st.number_input("Enter number", step=1)

    if st.button("Show Table"):
        for i in range(1, 11):
            st.write(f"{num} x {i} = {num*i}")


elif option == "9. Multiplication Table of 9":
    if st.button("Show Table"):
        for i in range(1, 11):
            st.write(f"9 x {i} = {9*i}")


elif option == "10. Sum of Digits":
    num = st.number_input("Enter number", step=1)

    if st.button("Find Sum"):
        temp = int(num)
        total = 0

        while temp > 0:
            digit = temp % 10
            total += digit
            temp = temp // 10

        st.success(f"Sum of digits = {total}")


elif option == "11. Factorial of a Number":
    num = st.number_input("Enter number", step=1)

    if st.button("Find Factorial"):
        fact = 1

        for i in range(1, int(num)+1):
            fact *= i

        st.success(f"Factorial = {fact}")


elif option == "12. Factors of a Number":
    num = st.number_input("Enter number", step=1)

    if st.button("Find Factors"):
        st.write("Factors are:")

        for i in range(1, int(num)+1):
            if num % i == 0:
                st.write(i)


elif option == "13. Prime Number Check":
    num = st.number_input("Enter number", step=1)

    if st.button("Check Prime"):
        count = 0

        for i in range(1, int(num)+1):
            if num % i == 0:
                count += 1

        if count == 2:
            st.success("Prime Number")
        else:
            st.error("Not a Prime Number")


elif option == "14. Sum of Elements in a List":
    nums = st.text_input("Enter numbers separated by commas")

    if st.button("Find Sum"):
        numbers = list(map(int, nums.split(",")))
        st.success(f"Sum = {sum(numbers)}")


elif option == "15. Student Grade Calculation":
    name = st.text_input("Enter student name")

    maths = st.number_input("Maths Marks")
    physics = st.number_input("Physics Marks")
    chemistry = st.number_input("Chemistry Marks")

    if st.button("Calculate Grade"):
        total = maths + physics + chemistry
        avg = total / 3

        st.write("Student Name:", name)
        st.write("Total Marks:", total)

        if avg >= 90:
            grade = "A"
        elif avg >= 75:
            grade = "B"
        elif avg >= 50:
            grade = "C"
        else:
            grade = "Fail"

        st.success(f"Grade = {grade}")


elif option == "16. Read CSV Using Pandas":

    uploaded_file = st.file_uploader("Upload CSV File", type=["csv"])

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)

        st.write("First 10 Records")
        st.dataframe(df.head(10))
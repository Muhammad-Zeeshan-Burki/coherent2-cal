import streamlit as st
import math

# Basic arithmetic operations
def basic_operations(num1, num2, operation):
    if operation == 'Addition':
        return num1 + num2
    elif operation == 'Subtraction':
        return num1 - num2
    elif operation == 'Multiplication':
        return num1 * num2
    elif operation == 'Division':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error! Division by zero."

# Trigonometric operations
def trigonometric_operations(angle, function):
    radians = math.radians(angle)
    if function == 'Sine':
        return math.sin(radians)
    elif function == 'Cosine':
        return math.cos(radians)
    elif function == 'Tangent':
        return math.tan(radians)

# Logarithmic operations
def logarithmic_operations(num):
    if num > 0:
        return math.log(num), math.log10(num)
    else:
        return "Error! Logarithm of non-positive numbers is undefined."

# Power and factorial operations
def power_factorial_operations(num, exp=None, operation=None):
    if operation == 'Power':
        return math.pow(num, exp)
    elif operation == 'Factorial':
        if num >= 0:
            return math.factorial(num)
        else:
            return "Error! Factorial of negative numbers is undefined."

# Streamlit Interface
st.title("Python Calculator")

# Selection of calculator type
calc_type = st.sidebar.selectbox("Select Operation Type", 
                                 ("Basic Operations", "Trigonometric Functions", 
                                  "Logarithms", "Power & Factorial"))

# Basic Operations
if calc_type == "Basic Operations":
    st.subheader("Basic Operations")
    num1 = st.number_input("Enter first number", format="%f")
    num2 = st.number_input("Enter second number", format="%f")
    operation = st.selectbox("Choose operation", ('Addition', 'Subtraction', 'Multiplication', 'Division'))
    result = basic_operations(num1, num2, operation)
    st.write(f"Result: {result}")

# Trigonometric Functions
elif calc_type == "Trigonometric Functions":
    st.subheader("Trigonometric Functions")
    angle = st.number_input("Enter angle in degrees", format="%f")
    function = st.selectbox("Choose function", ('Sine', 'Cosine', 'Tangent'))
    result = trigonometric_operations(angle, function)
    st.write(f"Result: {result}")

# Logarithms
elif calc_type == "Logarithms":
    st.subheader("Logarithmic Functions")
    num = st.number_input("Enter a positive number", format="%f")
    if st.button("Calculate Logarithms"):
        natural_log, base10_log = logarithmic_operations(num)
        st.write(f"Natural log of {num}: {natural_log}")
        st.write(f"Base-10 log of {num}: {base10_log}")

# Power & Factorial
elif calc_type == "Power & Factorial":
    st.subheader("Power & Factorial Functions")
    operation = st.selectbox("Choose operation", ('Power', 'Factorial'))
    
    if operation == 'Power':
        base = st.number_input("Enter base number", format="%f")
        exponent = st.number_input("Enter exponent", format="%f")
        result = power_factorial_operations(base, exponent, operation='Power')
        st.write(f"Result: {result}")
    
    elif operation == 'Factorial':
        num = st.number_input("Enter a non-negative integer", format="%d")
        result = power_factorial_operations(num, operation='Factorial')
        st.write(f"Result: {result}")

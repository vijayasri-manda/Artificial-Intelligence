import streamlit as st
import math

st.title("🧮 Advanced Calculator")

# Session state for memory and history
if "memory" not in st.session_state:
    st.session_state.memory = 0
if "history" not in st.session_state:
    st.session_state.history = []

def add_history(expression, result):
    st.session_state.history.append(f"{expression} = {result}")

def clear_history():
    st.session_state.history = []

# Input number 1
num1 = st.number_input("Enter first number", format="%.8f")

# Select operation
operation = st.selectbox("Select operation", [
    "Add (+)",
    "Subtract (-)",
    "Multiply (×)",
    "Divide (÷)",
    "Power (^)",
    "Square root (√)",
    "Factorial (!)",
    "Sine (sin)",
    "Cosine (cos)",
    "Tangent (tan)",
    "Natural Log (ln)",
    "Log base 10 (log)"
])

# Optional second number for unary operations
if operation in ["Square root (√)", "Factorial (!)", "Sine (sin)", "Cosine (cos)", "Tangent (tan)", "Natural Log (ln)", "Log base 10 (log)"]:
    num2 = None
else:
    num2 = st.number_input("Enter second number", format="%.8f")

result = None
error = None

try:
    if st.button("Calculate"):
        if operation == "Add (+)":
            result = num1 + num2
            add_history(f"{num1} + {num2}", result)
        elif operation == "Subtract (-)":
            result = num1 - num2
            add_history(f"{num1} - {num2}", result)
        elif operation == "Multiply (×)":
            result = num1 * num2
            add_history(f"{num1} × {num2}", result)
        elif operation == "Divide (÷)":
            if num2 == 0:
                error = "Error: Division by zero!"
            else:
                result = num1 / num2
                add_history(f"{num1} ÷ {num2}", result)
        elif operation == "Power (^)":
            result = num1 ** num2
            add_history(f"{num1} ^ {num2}", result)
        elif operation == "Square root (√)":
            if num1 < 0:
                error = "Error: Square root of negative number!"
            else:
                result = math.sqrt(num1)
                add_history(f"√{num1}", result)
        elif operation == "Factorial (!)":
            if not num1.is_integer() or num1 < 0:
                error = "Error: Factorial only defined for non-negative integers!"
            else:
                result = math.factorial(int(num1))
                add_history(f"{int(num1)}!", result)
        elif operation == "Sine (sin)":
            result = math.sin(math.radians(num1))
            add_history(f"sin({num1}°)", result)
        elif operation == "Cosine (cos)":
            result = math.cos(math.radians(num1))
            add_history(f"cos({num1}°)", result)
        elif operation == "Tangent (tan)":
            result = math.tan(math.radians(num1))
            add_history(f"tan({num1}°)", result)
        elif operation == "Natural Log (ln)":
            if num1 <= 0:
                error = "Error: ln undefined for ≤ 0!"
            else:
                result = math.log(num1)
                add_history(f"ln({num1})", result)
        elif operation == "Log base 10 (log)":
            if num1 <= 0:
                error = "Error: log undefined for ≤ 0!"
            else:
                result = math.log10(num1)
                add_history(f"log({num1})", result)
except Exception as e:
    error = f"Error: {str(e)}"

if error:
    st.error(error)
elif result is not None:
    st.success(f"Result: {result}")

# Memory functions
st.markdown("---")
st.subheader("Memory")

mem_col1, mem_col2, mem_col3, mem_col4 = st.columns(4)
if mem_col1.button("M+"):
    if result is not None:
        st.session_state.memory += result
if mem_col2.button("M-"):
    if result is not None:
        st.session_state.memory -= result
if mem_col3.button("MR"):
    st.info(f"Memory Recall: {st.session_state.memory}")
if mem_col4.button("MC"):
    st.session_state.memory = 0
    st.info("Memory cleared.")

# Calculation history
st.markdown("---")
st.subheader("Calculation History")
if st.button("Clear History"):
    clear_history()
if st.session_state.history:
    for i, record in enumerate(reversed(st.session_state.history[-10:]), 1):
        st.write(f"{i}. {record}")
else:
    st.write("No history yet.")

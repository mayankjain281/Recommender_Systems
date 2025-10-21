# import streamlit as st

# st.title("🚀 Run Python Code on Button Click")

# st.write("Press the button below to execute a Python function.")

# # Define your Python function
# def my_function():
#     # Example code — you can replace this with any logic
#     result = sum([i**2 for i in range(1, 6)])  # 1²+2²+3²+4²+5² = 55
#     return f"✅ The result is: {result}"

# # Button to trigger the function
# if st.button("Run Code"):
#     output = my_function()
#     st.success(output)
# else:
#     st.info("Click the button to run the code.")



import streamlit as st
import pandas as pd

# --- Streamlit setup ---
st.set_page_config(page_title="Live Google Sheet Dashboard", layout="wide")
st.title("📊 Live Nifty500 Dashboard (Google Sheet Connected)")

# Define your Python function
def my_function():
    # Example code — you can replace this with any logic
    result = sum([i**2 for i in range(1, 6)])  # 1²+2²+3²+4²+5² = 55
    return f"✅ The result is: {result}"

# Button to trigger the function
if st.button("Run Code"):
    output = my_function()
    st.success(output)
else:
    st.info("Click the button to run the code.")
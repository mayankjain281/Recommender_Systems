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
st.set_page_config(page_title="Google Sheet Viewer", layout="wide")
st.title("📊 Public Google Sheet Data")

# --- Google Sheet public CSV link ---
# Replace this with your Google Sheet link
sheet_id = "1RrXZTkepGLw1XdLhutivAp3mwXSKRZPHC5bi-cmEBBg"  # Extracted from your link
sheet_name = "Sheet1"
sheet_url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"

# --- Fetch data ---
@st.cache_data  # caches the data so it doesn't reload every time
def load_data(url):
    df = pd.read_csv(url)
    return df

df = load_data(sheet_url)

# --- Display data ---
st.dataframe(df)  # shows an interactive table
st.write("Data Summary:")
st.write(df.describe())

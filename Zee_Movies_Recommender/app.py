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

# --- Google Sheet public CSV link ---
sheet_id = "https://docs.google.com/spreadsheets/d/1RrXZTkepGLw1XdLhutivAp3mwXSKRZPHC5bi-cmEBBg/edit?usp=sharing"  # 👈 replace with your ID
sheet_name = "Sheet1"       # 👈 change if needed
url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"

# --- Fetch data directly from Google Sheet ---
df = pd.read_csv(url)

# --- Display data ---
st.success("✅ Live data fetched from Google Sheet (public)")
st.dataframe(df, use_container_width=True)

# --- Example metrics or charts ---
# st.metric("Rows in Sheet", len(df))
# if "QualityScore" in df.columns:
#     st.metric("Avg Quality Score", round(df["QualityScore"].mean(), 2))

# streamlit run c:/Users/mayan/Desktop/Portfolio Projects/Recommender_Systems/Zee_Movies_Recommender/app.py

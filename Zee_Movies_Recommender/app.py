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
from st_aggrid import AgGrid  # optional, for interactive table

# --- Streamlit setup ---
st.set_page_config(page_title="Live Google Sheet Dashboard", layout="wide")
st.title("📊 Live Nifty500 Dashboard (Google Sheet Connected)")

# --- Google Sheet public CSV link ---
# Only the Sheet ID is needed, not full URL
sheet_id = "1RrXZTkepGLw1XdLhutivAp3mwXSKRZPHC5bi-cmEBBg"  # Extracted from your link
sheet_name = "Sheet1"
url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"

# --- Fetch data directly from Google Sheet ---
@st.cache_data(ttl=300)  # cache for 5 minutes
def load_data():
    df = pd.read_csv(url)
    df = df.apply(pd.to_numeric, errors='ignore')  # convert numeric columns
    return df

df = load_data()

# --- Display live metrics ---
st.success("✅ Live data fetched from Google Sheet (public)")
st.metric("Rows in Sheet", len(df))

if "QualityScore" in df.columns:
    st.metric("Avg Quality Score", round(df["QualityScore"].mean(), 2))

# --- Display table ---
st.subheader("📋 Data Table")
# Option 1: Streamlit native scrollable table
st.dataframe(df, width=1200, height=600)

# Option 2: Interactive AgGrid table (uncomment if installed)
# AgGrid(df)

# --- Optional: Auto-refresh info ---
st.info("Data is cached and auto-refreshes every 5 minutes.")


# streamlit run c:/Users/mayan/Desktop/Portfolio Projects/Recommender_Systems/Zee_Movies_Recommender/app.py
# new







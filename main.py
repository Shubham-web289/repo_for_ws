import streamlit as st
import pandas as pd

# App configuration
st.set_page_config(page_title="📁 Upload and Display File", layout="wide")
st.title("📄 Upload CSV or Excel File and Display")

# File uploader
uploaded_file = st.file_uploader("Choose a CSV or Excel file", type=["csv", "xlsx", "xls"])

# Read and display file
if uploaded_file is not None:
    try:
        # Try reading as Excel
        if uploaded_file.name.endswith((".xlsx", ".xls")):
            df = pd.read_excel(uploaded_file)
        else:
            df = pd.read_csv(uploaded_file)

        st.success(f"✅ Successfully loaded `{uploaded_file.name}`")
        st.write("### Preview of Uploaded Data:")
        st.dataframe(df, use_container_width=True)

    except Exception as e:
        st.error(f"❌ Error reading file: {e}")
else:
    st.info("📤 Please upload a file to get started.")

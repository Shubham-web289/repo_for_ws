import streamlit as st
import pandas as pd

st.set_page_config(page_title="File Upload Test", layout="centered")
st.title("🧪 Minimal Upload Test")

# Upload
uploaded_file = st.file_uploader("Upload CSV or Excel", type=["csv", "xlsx", "xls"])

# Process and display
if uploaded_file is not None:
    try:
        if uploaded_file.name.endswith(".csv"):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)

        st.success(f"✅ Successfully loaded `{uploaded_file.name}`")
        st.write("### First 5 Rows of Data:")
        st.dataframe(df.head(), use_container_width=True)

    except Exception as e:
        st.error(f"❌ Failed to read file: {e}")
else:
    st.info("📂 Please upload a file to test.")

# Optional: Display file size for debug
if uploaded_file is not None:
    st.caption(f"File size: {len(uploaded_file.getbuffer()) / 1024:.2f} KB")

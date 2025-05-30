import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="File Upload Test", layout="centered")
st.title("🧪 Minimal Upload Test")

import streamlit as st

# Path to requirements.txt (adjust if necessary)
file_path = "requirements.txt"

# Read and display the content
try:
    with open(file_path, "r") as file:
        content = file.read()
    st.subheader("📦 Contents of `requirements.txt`")
    st.code(content, language='text')
except FileNotFoundError:
    st.error(f"File not found: {file_path}")

file_path2 = "runtime.txt"

# Read and display the content
try:
    with open(file_path2, "r") as file:
        content = file.read()
    st.subheader("📦 Contents of `runtime.txt`")
    st.code(content, language='text')
except FileNotFoundError:
    st.error(f"File not found: {file_path2}")

# Upload



# Set a seed for reproducibility
np.random.seed(42)

# Create DataFrame
df = pd.DataFrame(
    np.random.randint(1, 100, size=(10, 5)),
    columns=['A', 'B', 'C', 'D', 'E']
)

st.write(df)


#st.text_area("Paste CSV Data Here")

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

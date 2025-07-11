from auth import check_password
if not check_password():
    st.stop()



# pages/3_Downloads.py
import streamlit as st

st.set_page_config(page_title="Download Reports", layout="wide")

theme = st.sidebar.radio("🌗 Theme", ["Light", "Dark"])
if theme == "Dark":
    st.markdown("""
        <style>
        body { background-color: #111; color: white; }
        .stApp { background-color: #111; color: white; }
        </style>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
        <style>
        body { background-color: #f5f5f5; color: black; }
        .stApp { background-color: #f5f5f5; color: black; }
        </style>
    """, unsafe_allow_html=True)

st.markdown("""
<div style='display: flex; justify-content: center; gap: 1rem; margin-bottom: 2rem;'>
    <a href="/Home" target="_self"><button style='padding: 8px 20px; border: none; border-radius: 5px; background-color: #4CAF50; color: white;'>🏠 Home</button></a>
    <a href="/Resume_Analyzer" target="_self"><button style='padding: 8px 20px; border: none; border-radius: 5px; background-color: #007bff; color: white;'>🔍 Resume Analyzer</button></a>
</div>
""", unsafe_allow_html=True)

st.markdown("""
    <h2 style='text-align: center;'>📅 Download or Export Analysis</h2>
""", unsafe_allow_html=True)

st.info("This page will let users download their report as PDF or CSV (coming soon).")

# Back Button
st.markdown("""
    <a href="/Home" target="_self">
        <button style='margin-top: 30px; padding: 10px 20px; border: none; border-radius: 8px; background-color: #6c757d; color: white;'>🔙 Back to Home</button>
    </a>
""", unsafe_allow_html=True)

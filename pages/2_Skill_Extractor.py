import streamlit as st
from auth import check_password

if not check_password():
    st.stop()

st.set_page_config(page_title="Skill Extractor", layout="wide")

# Theme Toggle
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

# Navigation Buttons
st.markdown("""
<div style='display: flex; justify-content: center; gap: 1rem; margin-bottom: 2rem;'>
    <a href="/Home" target="_self"><button style='padding: 8px 20px; border: none; border-radius: 5px; background-color: #4CAF50; color: white;'>🏠 Home</button></a>
    <a href="/JD_Insights" target="_self"><button style='padding: 8px 20px; border: none; border-radius: 5px; background-color: #007bff; color: white;'>📌 JD Insights</button></a>
    <a href="/Skill_Graph" target="_self"><button style='padding: 8px 20px; border: none; border-radius: 5px; background-color: #17a2b8; color: white;'>📊 Skill Graph</button></a>
    <a href="/Resume_Insights" target="_self"><button style='padding: 8px 20px; border: none; border-radius: 5px; background-color: #ffc107; color: white;'>📁 Resume Insights</button></a>
</div>
""", unsafe_allow_html=True)

# Title
st.markdown("""
    <h2 style='text-align: center;'>🧠 ML-based Skill Extractor (Coming Soon)</h2>
""", unsafe_allow_html=True)

st.info("This page will use NLP/ML models to extract skills intelligently from resumes.")

st.markdown("""
    <p>This feature is under development. Stay tuned for updates!<br>
    In the meantime, you can use the <b>Resume Analyzer</b> to match your resume with job descriptions and extract skills.</p>
""", unsafe_allow_html=True)

# Back Button
st.markdown("""
    <a href="/Home" target="_self">
        <button style='margin-top: 30px; padding: 10px 20px; border: none; border-radius: 8px; background-color: #6c757d; color: white;'>🔙 Back to Home</button>
    </a>
""", unsafe_allow_html=True)
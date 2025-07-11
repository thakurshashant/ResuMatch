import streamlit as st
from PIL import Image

st.set_page_config(page_title="ResuMatch | Home", layout="wide")

# --- Hero Section ---
st.markdown("""
    <div style='text-align: center; padding: 2rem 0;'>
        <h1 style='font-size: 3rem; color: #4B8BBE;'> Welcome to <span style="color:#306998;">ResuMatch</span></h1>
        <p style='font-size: 1.2rem; color: #555;'>Your AI-powered assistant for analyzing resumes against job descriptions using NLP and ML</p>
    </div>
""", unsafe_allow_html=True)

st.markdown("---")

# --- Features Section ---
st.subheader("🔧 What Does ResuMatch Do?")
cols = st.columns(3)
with cols[0]:
    st.markdown("### 🧠 Skill Extraction")
    st.markdown("- Extracts skills using intelligent tokenization & keyword matching.")
    st.markdown("- Identifies soft + technical skills from resume & JD.")

with cols[1]:
    st.markdown("### 📊 Cosine Similarity")
    st.markdown("- Converts both JD and resume into TF-IDF vectors.")
    st.markdown("- Computes cosine similarity between them.")
    st.markdown("- Gives a match % score.")

with cols[2]:
    st.markdown("### 🔍 Match Analysis")
    st.markdown("- Shows **Matched** vs **Missing** skills.")
    st.markdown("- Provides personalized **Recommendations**.")

st.markdown("---")

# --- Cosine Similarity Explanation ---
with st.expander("📐 How Does Cosine Similarity Work? (Click to Learn)"):
    st.markdown("""
    Cosine Similarity is a metric used to determine how similar two documents are, regardless of their size. It measures the cosine of the angle between two non-zero vectors of an inner product space.
    
    In **ResuMatch**, we:
    - Convert your **resume** and **job description** into numerical vectors using **TF-IDF**.
    - Then compute the **cosine** of the angle between them.
    
    #### Formula:
    \n
    \[
    \text{cosine similarity} = \frac{{A \cdot B}}{{||A|| \times ||B||}}
    \]
    
    - **A · B** = dot product of vectors A and B  
    - **||A|| and ||B||** = magnitudes (lengths) of the vectors
    
    #### Result:
    - **1.0** means documents are identical in direction (very similar).
    - **0.0** means documents are orthogonal (no similarity).
    """)

# --- Skill Matching Explanation ---
with st.expander("🎯 How Skill Matching Works?"):
    st.markdown("""
    - The system uses a **predefined intelligent skill list** with 100+ technical & soft skills.
    - Your resume and JD text are scanned using **regular expressions** and **NLP**.
    - Then it compares the sets:
        - Skills found in Resume ✅
        - Skills required in JD 📄
        - And finds:
            - ✅ **Matched Skills**
            - ❌ **Missing Skills**
    
    The final match % is based on:
    \n
    \[
    \text{match\_percent} = \frac{{\text{# matched skills}}}{{\text{# JD skills}}} \times 100
    \]
    """)

# --- Call to Action ---
st.markdown("---")
st.markdown("""
    <div style='text-align: center; padding-top: 1rem;'>
        <h3>Ready to see how well your resume matches?</h3>
        <a href='/Resume_Analyzer' target='_self' style='text-decoration: none;'>
            <button style='font-size: 1.1rem; padding: 0.7rem 1.5rem; background-color: #4B8BBE; color: white; border: none; border-radius: 8px; margin-top: 10px;'>Analyze Now</button>
        </a>
    </div>
""", unsafe_allow_html=True)

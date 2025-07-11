import streamlit as st
import os
import tempfile
import time
import pandas as pd

from utils.similarity import calculate_similarity
from utils.text_cleaner import clean_text
from utils.ner_extractor import extract_entities
from utils.text_extraction import extract_text_from_pdf
from utils.skills_matching import (
    identification_keywords,
    extracting_skills,
    comparison_logic
)

# Page configuration
st.set_page_config(page_title="Resume Analyzer", layout="wide")
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>📄 AI-Powered Resume Analyzer</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Analyze your resume against a job description using NLP, Skill Matching, and TF-IDF similarity.</p>", unsafe_allow_html=True)

# File and JD upload section
st.markdown("---")
col1, col2 = st.columns(2)

with col1:
    st.subheader("📤 Upload Your Resume")
    resume_file = st.file_uploader("Upload PDF", type=["pdf"])

with col2:
    st.subheader("📝 Paste Job Description")
    jd_text = st.text_area("Paste the job description here", height=200)

# Analyzer logic
def analyze_resume(resume_file, jd_text):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(resume_file.read())
        tmp_path = tmp.name

    resume_text = clean_text(extract_text_from_pdf(tmp_path))
    jd_text_clean = clean_text(jd_text)

    entities = extract_entities(resume_text)
    resume_skills = extracting_skills(resume_text)
    jd_skills = extracting_skills(jd_text_clean)
    keywords = identification_keywords(resume_text)
    matched, missing, match_percent = comparison_logic(resume_skills, jd_skills)
    similarity_score = calculate_similarity(resume_text, jd_text_clean)

    os.remove(tmp_path)
    return resume_skills, keywords, entities, matched, missing, match_percent, similarity_score, jd_skills

# Trigger analysis
st.markdown("---")
if st.button("🔍 Analyze Resume", use_container_width=True):
    if not resume_file or not jd_text:
        st.warning("⚠️ Please upload a resume and paste the job description.")
    else:
        with st.spinner("Analyzing your resume using AI and NLP..."):
            time.sleep(1.5)
            try:
                resume_skills, keywords, entities, matched, missing, match_percent, similarity_score, jd_skills = analyze_resume(resume_file, jd_text)
            except Exception as e:
                st.error(f"An error occurred: {e}")
                st.stop()

        st.success("✅ Analysis Complete!")

        # Cosine Similarity Score
        st.markdown("### 📐 Similarity Score")
        st.metric(label="Cosine Similarity", value=f"{similarity_score}%", help="Similarity between your resume and the job description")
        st.progress(int(similarity_score))

        # Expanding Sections
        with st.expander("🧠 Named Entities Extracted"):
            st.write(entities if entities else "No named entities found.")

        with st.expander("✅ Skills Found in Resume"):
            st.write(resume_skills if resume_skills else "No skills found in resume.")

        with st.expander("📄 Skills Required in Job Description"):
            st.write(jd_skills if jd_skills else "No skills found in JD.")

        with st.expander("📌 Important Keywords in Resume"):
            st.write(keywords if keywords else "No important keywords found.")

        # Matched / Missing Skills
        st.markdown("### 🧩 Skills Comparison")

        col1, col2 = st.columns(2)
        with col1:
            st.markdown("#### ✅ Matched Skills")
            if matched:
                st.dataframe(pd.DataFrame(matched, columns=["Skill"]), use_container_width=True)
            else:
                st.info("No matched skills found.")

        with col2:
            st.markdown("#### ❌ Missing Skills")
            if missing:
                st.dataframe(pd.DataFrame(missing, columns=["Skill"]), use_container_width=True)
            else:
                st.success("Your resume covers all JD skills! 💪")

        # Summary Scorecard
        st.markdown("### 📊 Overall Match Summary")
        st.metric("Match Percentage", f"{match_percent:.2f}%")

        if match_percent >= 80:
            level, color, emoji = "Excellent", "#28a745", "✅"
        elif match_percent >= 50:
            level, color, emoji = "Moderate", "#ffc107", "⚠️"
        else:
            level, color, emoji = "Low", "#dc3545", "❌"

        st.markdown(
            f"<div style='padding: 1rem; background-color: {color}; color: white; border-radius: 10px;'>"
            f"<h5 style='margin:0;'>{emoji} <b>Match Level:</b> {level} ({match_percent:.2f}%)</h5>"
            f"</div>",
            unsafe_allow_html=True
        )
        st.progress(int(match_percent))

        # Recommendations
        st.markdown("### 💡 Recommendations")
        if missing:
            st.info("To improve your resume, consider adding the following skills:")
            for skill in missing:
                st.markdown(f"- 🔧 **{skill}**")
        else:
            st.success("Awesome! Your resume already includes all required skills. 🎉")

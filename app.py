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

# ---------------- Streamlit Page Config ----------------
st.set_page_config(page_title="ResuMatch - JD Analyzer", layout="wide")
st.title("📄 ResuMatch – Resume & JD Skill Analyzer")

# ---------------- Input Section ----------------
st.header("1. Upload Your Resume")
resume_file = st.file_uploader("Upload a PDF file", type=["pdf"])

st.header("2. Paste Job Description")
jd_text = st.text_area("Paste the job description here")

# ---------------- Analysis Logic ----------------
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

    os.remove(tmp_path)  # Cleanup
    return resume_skills, keywords, entities, matched, missing, match_percent, similarity_score, jd_skills

# ---------------- Run Analysis ----------------
if st.button("🔍 Analyze Resume"):
    if not resume_file or not jd_text:
        st.error("⚠️ Please upload a resume and paste the job description.")
    else:
        with st.spinner("Analyzing your resume..."):
            time.sleep(1.5)
            try:
                resume_skills, keywords, entities, matched, missing, match_percent, similarity_score, jd_skills = analyze_resume(resume_file, jd_text)
            except Exception as e:
                st.error(f"An error occurred during analysis: {e}")
                st.stop()

        st.success("✅ Resume analysis completed!")

        # ---------------- Output Section ----------------
        st.subheader("📐 TF-IDF Similarity Score")
        st.write(f"🧮 Cosine Similarity: `{similarity_score}%`")
        st.progress(int(similarity_score))

        st.subheader("🧠 Named Entities Extracted")
        st.write(entities if entities else "No entities found.")

        st.subheader("✅ Skills Found in Resume")
        st.write(resume_skills if resume_skills else "No skills identified in resume.")

        st.subheader("📄 Skills Required in JD")
        st.write(jd_skills if jd_skills else "No skills identified in JD.")

        st.subheader("📌 Keywords Found")
        st.write(keywords if keywords else "No important keywords found.")

        # ---------------- Matched and Missing Skills Section ----------------
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("📋 Matched Skills")
            if matched:
                matched_df = pd.DataFrame(matched, columns=["Skill"])
                st.dataframe(matched_df, use_container_width=True)
            else:
                st.info("No matched skills found.")

        with col2:
            st.subheader("❌ Missing Skills from JD")
            if missing:
                missing_df = pd.DataFrame(missing, columns=["Skill"])
                st.dataframe(missing_df, use_container_width=True)
            else:
                st.success("Your resume covers all required skills in JD! 💪")

        # ---------------- Match Summary ----------------
        st.subheader("📊 Overall Match Summary")
        st.metric(label="🔵 Match Score", value=f"{match_percent:.2f}%")

        if match_percent >= 80:
            level = "Excellent"
            color = "#28a745"  # Green
            emoji = "✅"
        elif match_percent >= 50:
            level = "Moderate"
            color = "#ffc107"  # Orange
            emoji = "⚠️"
        else:
            level = "Low"
            color = "#dc3545"  # Red
            emoji = "❌"

        st.markdown(
            f"<div style='padding: 1rem; background-color: {color}; color: white; border-radius: 10px;'>"
            f"<h5 style='margin:0;'>{emoji} <b>Match Level:</b> {level} ({match_percent:.2f}%)</h5>"
            f"</div>",
            unsafe_allow_html=True
        )
        st.progress(int(match_percent))

        # ---------------- Recommendations ----------------
        st.subheader("💡 Recommendations")
        if missing:
            st.info("Based on the job description, consider adding the following skills:")
            for skill in missing:
                st.markdown(f"- 🔧 **{skill}**")
        else:
            st.success("Your resume already includes all required skills! 🎉")

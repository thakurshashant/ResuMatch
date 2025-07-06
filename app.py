import streamlit as st
import os
import tempfile
import time

from utils.text_cleaner import clean_text
from utils.ner_extractor import extract_entities
from utils.text_extraction import extract_text_from_pdf
from utils.skills_matching import (
    identification_keywords,
    extracting_skills,
    extract_skills_from_jd,
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
    keywords = identification_keywords(resume_text)
    matched_skills = extract_skills_from_jd(jd_text_clean, resume_skills)
    matched, missing, match_percent = comparison_logic(resume_skills, matched_skills)

    os.remove(tmp_path)  # Cleanup
    return resume_skills, keywords, entities, matched, missing, match_percent

# ---------------- Run Analysis ----------------
if st.button("🔍 Analyze Resume"):
    if not resume_file or not jd_text:
        st.error("⚠️ Please upload a resume and paste the job description.")
    else:
        with st.spinner("Analyzing your resume..."):
            time.sleep(1.5)
            resume_skills, keywords, entities, matched, missing, match_percent = analyze_resume(resume_file, jd_text)

        st.success("✅ Resume analysis completed!")

        # ---------------- Output Section ----------------
        st.subheader("🧠 Named Entities Extracted")
        st.write(entities)

        st.subheader("✅ Skills Found in Resume")
        st.write(resume_skills)

        st.subheader("📌 Keywords Found")
        st.write(keywords)

        st.subheader("📋 Matched Skills")
        st.write(matched)

        st.subheader("❌ Missing Skills from JD")
        st.write(missing)

        st.subheader("📊 Match Percentage")
        st.write(f"🔵 {match_percent:.2f}%")
        st.progress(int(match_percent))

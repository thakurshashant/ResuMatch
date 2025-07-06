import streamlit as st

st.set_page_config(page_title="ResuMatch - JD Analyzer", layout="wide")

st.title("📄 ResuMatch – Resume & JD Skill Analyzer")

st.header("1. Upload Your Resume")
resume_file = st.file_uploader("Upload a PDF file", type=["pdf"])

st.header("2. Upload Job Description")
jd_text = st.text_area("Paste the job description here")

analyze = st.button("Analyze Resume")


if analyze:
    if not resume_file or not jd_text:
        st.error("Please upload a resume and paste the job description")
    else:
        with open("temp_resume.pdf", "wb") as f:
            f.write(resume_file.read())
        from utils.text_extraction import extract_text_from_pdf, read_jd_from_file
        from utils.skills_matching import (
            identification_keywords,
            extracting_skills,
            extract_skills_from_jd,
            comparison_logic
        )

        resume_text = extract_text_from_pdf("temp_resume.pdf").lower()
        jd_text = jd_text.lower()

        resume_skills = extracting_skills(resume_text)
        keywords = identification_keywords(resume_text)
        matched_skills = extract_skills_from_jd(jd_text, resume_skills)

        matched, missing, match_percent = comparison_logic(resume_skills, matched_skills)

        # Display results
        st.subheader("📊 Analysis Result")
        st.write(f"✅ **Match Percentage:** `{match_percent:.2f}%`")
        st.write("🟢 **Matched Skills:**", matched)
        st.write("🔴 **Missing Skills from JD:**", missing)
        st.write("🧠 **Identified Keywords:**", keywords)






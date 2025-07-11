
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.text_extraction import extract_text_from_pdf, read_jd_from_file
from utils.skills_matching import (
    extracting_skills,
    identification_keywords,
    extract_skills_from_jd,
    comparison_logic,
)



if __name__ == "__main__":
    resume_path = "data/Shashant_Thakur.pdf"
    jd_path = "data/sample_jd.txt"

    extracted_text = extract_text_from_pdf(resume_path).lower()
    jd_text = read_jd_from_file(jd_path)

    resume_skills = extracting_skills(extracted_text)
    print("Skills Found:", resume_skills)

    identified_keywords = identification_keywords(extracted_text)
    print("Identified Keywords:", identified_keywords)

    matched_skills = extract_skills_from_jd(jd_text, resume_skills)
    print("Matched Skills from JD:", matched_skills)

    matched, missing, match_percent = comparison_logic(resume_skills, matched_skills)
    print("Comparison Logic Result:")
    print("Matched Skills:", matched)
    print("Missing Skills:", missing)
    print("Match Percentage:", match_percent, "%")

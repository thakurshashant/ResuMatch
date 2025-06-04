KNOWN_SKILLS = [
    "python", "java", "c++", "sql", "machine learning", "deep learning",
    "html", "css", "javascript", "aws", "docker", "react", "node.js",
    "django", "flask", "excel", "power bi", "git", "linux", "tensorflow"
]

def identification_keywords(extracted_text):
    keywords = ["Python", "Machine Learning", "Bachelor", "Master", "AWS", "React"]
    keywords = [k.lower() for k in keywords]

    words = extracted_text.split()
    keywords_founded = [word for word in words if word in keywords]
    
    return keywords_founded

def extracting_skills(extracted_text):
    extracted_text = extracted_text.lower()
    return [skill for skill in KNOWN_SKILLS if skill.lower() in extracted_text]

def extract_skills_from_jd(jd_text, resume_skills):
    jd_text = jd_text.lower()
    return [skill for skill in resume_skills if skill.lower() in jd_text]

def comparison_logic(resume_skills, jd_skills):
    matched = list(set(resume_skills) & set(jd_skills))
    missing = list(set(jd_skills) - set(resume_skills))
    match_percent = (len(matched) / len(jd_skills)) * 100 if jd_skills else 0

    return sorted(matched), sorted(missing), match_percent

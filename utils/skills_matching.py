


import re
# Predefined known skills for comparison
KNOWN_SKILLS = [
    # Programming Languages
    "python", "java", "c++", "c", "javascript", "typescript", "go", "ruby", "kotlin", "swift", "php", "r", "scala",

    # Web Development
    "html", "css", "react", "angular", "vue", "node.js", "express.js", "next.js", "tailwind css", "bootstrap", "jquery",

    # Backend & Frameworks
    "django", "flask", "spring", "laravel", "rails", "fastapi", "nest.js", "asp.net",

    # Databases
    "mysql", "postgresql", "mongodb", "oracle", "redis", "sqlite", "firebase", "dynamodb",

    # DevOps & Tools
    "docker", "kubernetes", "jenkins", "github actions", "ansible", "terraform", "prometheus", "grafana", "nginx",

    # Cloud Platforms
    "aws", "azure", "google cloud", "gcp", "heroku", "vercel", "netlify",

    # Data Science & ML
    "machine learning", "deep learning", "tensorflow", "keras", "pytorch", "scikit-learn", "numpy", "pandas",
    "matplotlib", "seaborn", "xgboost", "lightgbm", "nltk", "spacy", "opencv", "h2o.ai",

    # Big Data & Analytics
    "hadoop", "spark", "kafka", "hive", "pig", "airflow", "snowflake", "databricks", "power bi", "tableau", "excel",

    # Mobile & Cross Platform
    "android", "react native", "flutter", "xamarin", "swift", "kotlin",

    # Cybersecurity
    "wireshark", "nmap", "metasploit", "burpsuite", "splunk", "siem", "owasp",

    # Other Tools & Skills
    "git", "linux", "jira", "figma", "postman", "api testing", "ci/cd", "agile", "scrum"
]



# Identifies basic important keywords in the resume
def identification_keywords(extracted_text):
    KEYWORDS = [
    # Education
    "bachelor", "b.tech", "bsc", "b.e", "be", "mtech", "m.tech", "mca", "msc", "phd", "diploma", "graduate", "postgraduate",
    
    # Certifications & Courses
    "certification", "certified", "udemy", "coursera", "edx", "aws certified", "google certified", "oracle certified",

    # Roles / Titles
    "software engineer", "data scientist", "data analyst", "web developer", "android developer",
    "full stack developer", "frontend", "backend", "ml engineer", "ai engineer", "cloud engineer",

    # Technologies / Platforms
    "aws", "azure", "gcp", "google cloud", "devops", "docker", "kubernetes", "tensorflow", "pytorch",
    "react", "node.js", "django", "flask", "git", "github", "firebase", "sql", "nosql", "api",

    # Methodologies
    "agile", "scrum", "ci", "cd", "continuous integration", "continuous deployment",

    # Tools
    "jira", "figma", "postman", "vscode", "linux", "ubuntu", "power bi", "tableau",

    # Soft Skills & General
    "leadership", "communication", "teamwork", "problem solving", "collaboration"
    ]

    KEYWORDS = [k.lower() for k in KEYWORDS]

    words = extracted_text.split()
    keywords_founded = [word for word in words if word in KEYWORDS]
    
    return keywords_founded


# Extracts known technical skills from resume
def extracting_skills(extracted_text):
    words = set(re.findall(r'\b\w[\w.+#]*\b', extracted_text.lower()))
    found_skills = []

    for skill in KNOWN_SKILLS:
        tokens = set(skill.lower().split())
        if tokens.issubset(words):
            found_skills.append(skill)

    return found_skills

# Matches resume skills against skills in the JD
def extract_skills_from_jd(jd_text, resume_skills):
    jd_text = jd_text.lower()
    return [skill for skill in resume_skills if skill.lower() in jd_text]

# Compares and returns matched, missing, and match percentage
def comparison_logic(resume_skills, jd_skills):
    matched = list(set(resume_skills) & set(jd_skills))
    missing = list(set(jd_skills) - set(resume_skills))
    match_percent = (len(matched) / len(jd_skills)) * 100 if jd_skills else 0

    return sorted(matched), sorted(missing), match_percent

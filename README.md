# 🧠 ResuMatch – Resume vs JD Skill Analyzer

ResuMatch is an AI-powered tool that compares a candidate's resume against a job description to analyze skill match, highlight missing skills, and suggest improvements.

## 🚀 Features

- Upload a PDF resume and paste a job description
- Extracts skills and keywords from resume
- Compares with JD to show:
  - ✅ Matched Skills
  - 🔴 Missing Skills
  - 📊 Match Percentage
- Clean, simple UI using Streamlit

## 🛠 Tech Stack

- Python
- Streamlit
- pdfplumber (for PDF parsing)
- pandas (optional for future UI tables)

## 📦 Folder Structure

ResuMatch/
│
├── app.py # Streamlit UI
├── data/ # Resume PDFs and JD text files
├── utils/ # All logic modules
│ ├── text_extraction.py
│ └── skills_matching.py
├── src/ # (Optional: Legacy or main script)
├── README.md
├── .gitignore
└── requirements.txt # (You can generate this)

markdown
Copy
Edit

## 📄 How to Run

1. Clone the repo  
2. Set up a virtual environment  
3. Install dependencies:

```bash
pip install streamlit pdfplumber
Run the app:

bash
Copy
Edit
streamlit run app.py

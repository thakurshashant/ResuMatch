import pdfplumber


# Extracts raw text from a PDF resume
def extract_text_from_pdf(file_path):
    text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text



# Reads and returns job description text from a file
def read_jd_from_file(jd_file_path):
    with open(jd_file_path, "r") as file:
        return file.read().lower()

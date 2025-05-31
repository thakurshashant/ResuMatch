import pdfplumber 

def extract_text_from_pdf(file_path):
    text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text


def identification_keyboard(extracted_text):
    keywords = [ "Python", "Machine Learning", "Bachelor", "Master", "AWS", "React"]
    keywords_founded = []

    words = extracted_text.split()

    for word in words:
        if word in keywords:
            keywords_founded.append(word)
    return keywords_founded






if __name__ == "__main__":
    file_path = "data/Shashant_Thakur.pdf"
    extracted_text = extract_text_from_pdf(file_path)
    print(extracted_text)

    identified_keywords = identification_keyboard(extracted_text)
    print(identified_keywords)

import re

def clean_text(text):
    """
    Cleans extracted resume or JD text:
    - Removes newlines, tabs, extra spaces
    - Removes punctuation
    - Converts to lowercase
    """
    text = text.lower()
    text = re.sub(r'\n', ' ', text)                # Remove newlines
    text = re.sub(r'\t', ' ', text)                # Remove tabs
    text = re.sub(r'[^\w\s]', '', text)            # Remove punctuation
    text = re.sub(r'\s+', ' ', text).strip()       # Remove extra spaces
    return text

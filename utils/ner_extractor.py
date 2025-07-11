
import spacy

nlp = spacy.load("en_core_web_sm")


def extract_entities(text):
    """
    Uses spaCy to extract named entities from resume text.
    Returns a list of (entity text, entity label) tuples.
    """
    doc = nlp(text)
    return [(ent.text, ent.label_) for ent in doc.ents]


def extract_qualifications(text):
    """
    Returns degrees or educational qualifications using NER.
    """
    doc = nlp(text)
    qualifications = []

    for ent in doc.ents:
        if ent.label_ in ["EDUCATION", "ORG", "WORK_OF_ART", "PERSON"]:
            qualifications.append(ent.text)

    return list(set(qualifications))
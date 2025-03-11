import spacy

# Load the English NLP model
nlp = spacy.load("en_core_web_sm")

def count_words(text: str) -> int:
    """Uses spaCy's tokenizer for efficient word counting."""
    doc = nlp(text)
    words = [token.text for token in doc if token.is_alpha or token.is_digit]
    return len(words)
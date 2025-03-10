def count_words(text: str) -> int:
    """Counts the number of words in the provided text."""
    # You can improve this by using regex to handle punctuation etc.
    return len(text.split())
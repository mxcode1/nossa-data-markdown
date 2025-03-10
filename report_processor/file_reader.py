def read_file(filepath: str) -> str:
    """Reads and returns the content of the file at the given path."""
    with open(filepath, 'r', encoding='utf-8') as file:
        return file.read()

import re
from typing import Dict, List

def extract_paragraphs_by_topic(text, topics):
    """
    Processes text line by line and maps each topic to a list of dictionaries
    containing the line number and corresponding paragraph.
    """
    topic_dict = {topic: [] for topic in topics}

    lines = text.split("\n")  # Split text by lines to track line numbers
    paragraph = []
    paragraph_start_line = None

    # Index indicates the Line Number while iterating through the available lines
    for line_number, line in enumerate(lines, start=1):
        if line.strip():  # Collect non-empty lines into a paragraph
            if paragraph_start_line is None:
                paragraph_start_line = line_number  # Store first line of paragraph
            paragraph.append(line.strip())
        else:
            if paragraph:  # Process paragraph when encountering an empty line
                paragraph_text = " ".join(paragraph)
                for topic in topics:
                    if topic.lower() in paragraph_text.lower():
                        topic_dict[topic].append({
                            "line_number": paragraph_start_line,
                            "text": paragraph_text
                        })
                paragraph = []  # Reset for next paragraph
                paragraph_start_line = None  # Reset start line

    # Handle last paragraph if text didn't end with a blank line
    if paragraph:
        paragraph_text = " ".join(paragraph)
        for topic in topics:
            if topic.lower() in paragraph_text.lower():
                topic_dict[topic].append({
                    "line_number": paragraph_start_line,
                    "text": paragraph_text
                })

    return topic_dict

# def extract_paragraphs_by_topic(text: str, topics: List[str]) -> Dict[str, List[str]]:
#     """
#     Extracts paragraphs that mention any of the given topics.
    
#     Args:
#         text: The full text content.
#         topics: A list of topic keywords.
        
#     Returns:
#         A dictionary mapping each topic to a list of paragraphs that mention it.
#     """
#     # Split text into paragraphs using blank lines (can be refined for rows in CSV-like files)
#     paragraphs = re.split(r'\n\s*\n', text)
#     topic_dict = {topic: [] for topic in topics}
    
#     for paragraph in paragraphs:
#         # For each topic, check if it appears in the paragraph (case-insensitive)
#         for topic in topics:
#             if topic.lower() in paragraph.lower():
#                 topic_dict[topic].append(paragraph.strip())
    
#     return topic_dict
import re
from typing import Dict, List

def extract_paragraphs_by_topic(text, topics):
    """
    Processes text line by line and maps each topic to a list of dictionaries
    containing the line number and corresponding paragraph.
    """
    topic_dict = {topic: [] for topic in topics}

    # Split text by lines to track line numbers
    lines = text.split("\n")  
    
    # Track paragraph boundaries when processing lines
    current_paragraph_lines = []
    paragraph_start_line = None
    
    # Iterate through all text in the file divided by line breaks
    for line_number, line in enumerate(lines, start=1):
        if line.strip():
            if paragraph_start_line is None:
                paragraph_start_line = line_number
            current_paragraph_lines.append(line.strip())
        else:
            if current_paragraph_lines:
                paragraph_text = " ".join(current_paragraph_lines)
                for topic in topics:
                    if topic.lower() in paragraph_text.lower():
                        # Store the actual text with original line breaks for verification
                        topic_dict[topic].append({
                            "line_number": paragraph_start_line,
                            "text": paragraph_text,
                        })
                current_paragraph_lines = []
                paragraph_start_line = None

    return topic_dict
import sys
import os
# Add the parent directory (project root) to the system path for tests
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from report_processor import topic_extractor


def test_extract_paragraphs_single_topic():
    # Single paragraph containing one topic.
    text = "This paragraph discusses Climate Risk Management in detail."
    topics = ["Climate Risk Management"]
    result = topic_extractor.extract_paragraphs_by_topic(text, topics)
    # Expect the topic key to have one matching paragraph.
    assert "Climate Risk Management" in result
    assert len(result["Climate Risk Management"]) == 1

def test_extract_paragraphs_multiple_paragraphs():
    # Multiple paragraphs where some mention one or more topics.
    text = (
        "Paragraph one discusses Scope 1 operations.\n\n"
        "Paragraph two foctopic_extractors on Health and wellness.\n\n"
        "Paragraph three mentions Scope 2 and Health challenges."
    )
    topics = ["Scope 1", "Scope 2", "Health"]
    result = topic_extractor.extract_paragraphs_by_topic(text, topics)
    # Verify that "Scope 1" is found in the first paragraph.
    assert len(result["Scope 1"]) == 1
    # "Scope 2" should appear once (in the third paragraph).
    assert len(result["Scope 2"]) == 1
    # "Health" should be found in both paragraph two and three.
    assert len(result["Health"]) == 2

def test_extract_paragraphs_no_topic():
    # Text does not contain any of the specified topics.
    text = "This paragraph does not mention any of the searched topics."
    topics = ["Climate Risk Management", "Water Risk Management"]
    result = topic_extractor.extract_paragraphs_by_topic(text, topics)
    # Expect empty lists for each topic.
    assert result["Climate Risk Management"] == []
    assert result["Water Risk Management"] == []

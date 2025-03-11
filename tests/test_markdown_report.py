import os
import pytest

from report_processor import file_reader
from report_processor import topic_extractor
from report_processor import word_counter


# Define the topics to search for
TOPICS = [
    "Climate Risk Management", 
    "Water Risk Management", 
    "Scope 1", 
    "Scope 2", 
    "Health", 
    "Employees", 
    "Forests"
]

@pytest.fixture
def test_markdown_path(tmp_path):
    """
    Fixture to create a temporary markdown file following the test report pattern.
    Returns the path to the created file.
    """
    content = (
        "# Test Report 2023\n\n"
        "## Table of Contents\n"
        "1. Introduction\n"
        "2. Sustainability Overview\n"
        "3. Climate Risk Management\n"
        "4. Water Risk Management\n"
        "5. Scope 1 Emissions\n"
        "6. Scope 2 Emissions\n"
        "7. Health and Safety\n"
        "8. Employees\n"
        "9. Forests and Biodiversity\n\n"
        "## Introduction\n"
        "This test report is created to validate our file reading, word counting, and topic extraction functions.\n\n"
        "## Sustainability Overview\n"
        "The report outlines our sustainability strategy and the steps taken to reduce environmental impacts.\n\n"
        "## Climate Risk Management\n"
        "Our climate risk management initiatives include measures to mitigate potential physical and transition risks due to climate change.\n\n"
        "## Water Risk Management\n"
        "We have implemented comprehensive water risk management policies to ensure efficient water use.\n\n"
        "## Scope 1 Emissions\n"
        "Detailed information regarding Scope 1 emissions is provided in this section.\n\n"
        "## Scope 2 Emissions\n"
        "The report also discusses Scope 2 emissions and strategies for reduction.\n\n"
        "## Health and Safety\n"
        "Health and safety remain a core priority with rigorous protocols in place.\n\n"
        "## Employees\n"
        "Our employees are our greatest asset, and we invest heavily in their well-being and development.\n\n"
        "## Forests and Biodiversity\n"
        "We are committed to preserving forests and promoting biodiversity across our operational footprint.\n"
    )
    file_path = tmp_path / "test_report.md"
    file_path.write_text(content, encoding="utf-8")
    return str(file_path)

def test_file_reader_with_test_markdown(test_markdown_path):
    """
    Test that the file_reader correctly reads the test markdown file.
    """
    content = file_reader.read_file(test_markdown_path)
    # Check that the content contains a known heading.
    assert "Test Report 2023" in content
    assert "## Climate Risk Management" in content

def test_word_counter_with_test_markdown(test_markdown_path):
    """
    Test the word counting function using the test markdown file.
    """
    content = file_reader.read_file(test_markdown_path)
    word_count = word_counter.count_words(content)
    # As this is a fixed test file, we check for a non-zero count.
    assert word_count > 50

def test_topic_extractor_with_test_markdown(test_markdown_path):
    """
    Test that the topic extractor can identify and return paragraphs for each topic in the test markdown file.
    """
    content = file_reader.read_file(test_markdown_path)
    topics_result = topic_extractor.extract_paragraphs_by_topic(content, TOPICS)
    
    # Verify that each topic key exists in the result dictionary.
    for topic in TOPICS:
        assert topic in topics_result
    
    # Check that paragraphs are extracted correctly for some topics:
    # For example, "Climate Risk Management" should have at least one paragraph.
    assert len(topics_result["Climate Risk Management"]) >= 1
    # Similarly for "Water Risk Management".
    assert len(topics_result["Water Risk Management"]) >= 1
    
    # For "Employees", check if the paragraph contains the expected text.
    employee_paragraphs = topics_result["Employees"]
    assert any("employees are our greatest asset" in para["text"].lower() for para in employee_paragraphs)
    
    # Check that the data structure includes the required fields
    for topic in TOPICS:
        for paragraph in topics_result[topic]:
            assert "line_number" in paragraph
            assert "text" in paragraph
            assert isinstance(paragraph["line_number"], int)
            assert isinstance(paragraph["text"], str)
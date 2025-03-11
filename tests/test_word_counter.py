import sys
import os
# Add the parent directory (project root) to the system path for tests
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from report_processor import word_counter

def test_count_words_simple():
    # Test a simple sentence with two words.
    text = "Hello world"
    # Expected: 2 words.
    assert word_counter.count_words(text) == 2

def test_count_words_multiple_spaces():
    # Test with extra spaces between words.
    text = "Hello    world   and   universe"
    # Expected: 4 words.
    assert word_counter.count_words(text) == 4

def test_count_words_empty_string():
    # Test with an empty string should return 0.
    text = ""
    assert word_counter.count_words(text) == 0

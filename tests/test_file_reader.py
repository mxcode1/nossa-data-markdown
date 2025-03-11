import sys
import os
# Add the parent directory (project root) to the system path for tests
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from report_processor import file_reader

def test_read_file(tmp_path):
    # Create a temporary file with known content.
    content = "Sample content for testing file reading."
    file = tmp_path / "test_file.txt"
    file.write_text(content, encoding="utf-8")
    
    # file_reader read_file to read the content back.
    read_content = file_reader.read_file(str(file))
    assert read_content == content

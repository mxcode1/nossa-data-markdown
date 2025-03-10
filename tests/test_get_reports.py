import sys
import os
# Add the parent directory (project root) to the system path for tests
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from report_processor import get_reports

def test_get_reports():
    # Call the Report Reader to extract the list of all report files in the reports directory
    files = get_reports.get_report_files()

    assert len(files) > 0
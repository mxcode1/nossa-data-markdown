import os 

def get_report_files(directory="reports"):
    """
    Returns a list of file paths for all markdown files in the specified directory.
    The directory is assumed to be relative to this script's location.
    """
    # Get the absolute path to the reports directory relative to this file
    reports_path = os.path.join(os.path.dirname(__file__), directory)
    
    # List all files in the reports directory that end with '.md'
    report_files = [
        os.path.join(reports_path, file)
        for file in os.listdir(reports_path)
        if file.endswith('.md')
    ]
    return report_files
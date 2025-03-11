Markdown Scraper Docs

This Python application scans Markdown (.md) reports, extracts relevant information, and generates a structured JSON report.

This JSON could be parsed or integrated with other data systems or tools to use the data in production

The output JSON includes:

    File details (name, path, word count)
    Extracted paragraphs, grouped by topics
    Line numbers for topic mentions

📂 Project Structure
````
report_processor/
├── output/                      # Folder where JSON data reports are saved with UID / Timestamp
│   ├── nossa_json_report_2025-03-10_19-13-31.json
├── reports/                     # Source Folder for providing Markdown reports for Analysis / Batch Processing
│   ├── bluewave_report.md
│   ├── ecotech_report.md
│   ├── globaltrade_report.md
├── tests/                        # Folder containing Pytest scripts
│   ├── __init__.py               # Marks the tests folder as a package
│   ├── test_file_reader.py        # Unit tests for file reading
│   ├── ....
├── report_processor/              # Main processing package
│   ├── __init__.py                # Marks report_processor as a package
│   ├── main.py                    # Main Driver script to run application and analyse reports
│   ├── file_reader.py             # Reads Markdown files
│   ├── get_reports.py             # Retrieves report files
│   ├── topic_extractor.py         # Extracts paragraphs mentioning key topics
│   ├── word_counter.py            # Counts words accurately
├── README.md                      # Project documentation
├── requirements.txt               # Install external dependencies 
````
🚀 How to Run the App

### Install Python (If Not Installed)

Install Python 3.11 

Check using: python --version

### Clone the Repository

git clone https://github.com/mxcode1/nossa-data-markdown
cd markdown-scraper

### Install Dependencies / Requrements.text

To install spacy and pytest dependencies use the provided requirements.txt

pip install -r requirements.txt

### Pytest 

For future development - Pytest test cases have been setup to verify changes to the different modules and functions

These tests can be run to verify code updates using Pytest (configured for Python 3.11)

### Run The Application (in /report_processor sub directory)

python main.py

### View the Generated JSON

After running the script, the JSON output will be saved inside the /output folder
You can use a JSON viewer such as https://jsonviewer.stack.hu/# to review the structure of the data output

Example Data Report:

output/nossa_json_report_2025-03-10_14-35-22.json

📝 JSON Output Structure

The generated JSON follows this structure:

```Example JSON Output
{
  "reports": [
    {
      "id": 1,
      "name": "greencorp_report.md",
      "file_path": "file:///absolute/path/to/reports/greencorp_report.md",
      "word_count": 3456,
      "topics": {
        "Climate Risk Management": [
          {
            "line_number": 12,
            "text": "Our Climate Risk Management framework includes mitigation strategies."
          }
        ],
        "Water Risk Management": [
          {
            "line_number": 45,
            "text": "Water Risk Management has led to a 30% reduction in water usage."
          }
        ],
        "Scope 1": [],
        "Scope 2": [],
        "Health": [
          {
            "line_number": 89,
            "text": "Employee health programs now include mental wellness support."
          }
        ],
        "Employees": [
          {
            "line_number": 105,
            "text": "We prioritize employees' well-being by offering flexible work arrangements."
          }
        ],
        "Forests": []
      }
    }
  ]
}
```

🔹 Explanation of JSON Fields
| Field | Description |
|-------|-------------|
| `id` | Unique ID for the report |
| `name` | Filename of the report |
| `file_path` | Absolute path to the file |
| `word_count` | Total number of words in the report |
| `topics` | Dictionary grouping extracted paragraphs by topic |
| `line_number` | Line number where the topic is mentioned |
| `text` | The paragraph mentioning the topic |

Markdown Scraper
📌 Overview

This Python application scans Markdown (.md) reports, extracts relevant information, and generates a structured JSON report.

The output JSON includes:

    File details (name, path, word count)
    Extracted paragraphs, grouped by topics
    Line numbers for topic mentions

📂 Project Structure

markdown-scraper/
├── reports/                    # Folder containing Markdown reports
│   ├── bluewave_report.md
│   ├── ecotech_report.md
│   ├── sunpower_report.md
│   └── ... (additional .md files)
├── output/                     # Folder where JSON reports are saved
│   ├── nossa_json_report_YYYY-MM-DD_HH-MM-SS.json
├── main.py                      # Main script to process reports
├── file_reader.py                # Reads Markdown files
├── word_counter.py               # Counts words accurately
├── topic_extractor.py            # Extracts paragraphs mentioning key topics
└── README.md                     # This documentation file

🚀 How to Run the App
1️⃣ Install Python (If Not Installed)

Make sure you have Python 3.6+ installed. Check using:

python --version

2️⃣ Clone the Repository

git clone https://github.com/mxcode1/markdown-scraper.git
cd markdown-scraper

3️⃣ Run the Script (from root directory)

python main.py

4️⃣ View the Generated JSON

After running the script, the JSON output will be saved inside the output/ folder
You can use a JSON viewer such as https://jsonviewer.stack.hu/# to review the structure of the data output

Example:

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

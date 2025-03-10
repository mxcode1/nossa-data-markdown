import os
import json
from datetime import datetime

import file_reader
import word_counter
import topic_extractor
import get_reports

def main():
    # File Output Paramaters
    output_directory_name = 'output'
    output_file_name = 'nossa_json_report'

    # List of report file paths (assumes the files are in the same directory)
    files = get_reports.get_report_files()
    
    # Topics to search for
    topics = [
        "Climate Risk Management", 
        "Water Risk Management", 
        "Scope 1", 
        "Scope 2", 
        "Health", 
        "Employees", 
        "Forests"
    ]
    
    for filepath in files:
        print(f"Processing file: {filepath}\n{'=' * 40}")
        content = file_reader.read_file(filepath)
        
        
        results = []

        for idx, file_path in enumerate(get_reports.get_report_files(), start=1):
            file_name = os.path.basename(file_path)
            content = file_reader.read_file(file_path)
            word_count = word_counter.count_words(content)
            paragraphs_by_topic = topic_extractor.extract_paragraphs_by_topic(content, topics)
            
            report_obj = {
                "id": idx,
                "name": file_name,
                "file_path": file_path,
                "word_count": word_count,
                "topics": paragraphs_by_topic
            }
            results.append(report_obj)

        # Create Output Directory and Timestamp for File Naming    
        os.makedirs(output_directory_name, exist_ok=True)
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        
        # Prepare Output / File Naming 
        output_path = os.path.join(output_directory_name, f'{output_file_name}_{timestamp}')
    
        # Create JSON Object
        output = {"reports": results}

        # Dump To File
        with open(output_path,"w",encoding="utf-8") as f:
            json.dump(output, f, indent=2)

        return json.dumps(output, indent=2)

if __name__ == '__main__':
    main()

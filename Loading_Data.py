import os
import json

COMBINE_FILE_PATH = r"C:\Users\Administrator\Desktop\AI Agents\combine_text_files.txt"
OUTPUT_FILE = r"C:\Users\Administrator\Desktop\AI Agents\extracted_data.json"

def extract_content_from_files(file_list_path):
    with open(file_list_path, 'r', encoding='utf-8') as file:
        filenames = [line.strip() for line in file]
    extracted_data = {}
    base_dir = os.path.dirname(file_list_path)

    for filename in filenames:
        file_path = os.path.join(base_dir, filename)
        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as f:
                extracted_data[filename] = f.read()
        else:
            print(f"File not found: {file_path}")
    return extracted_data

if __name__ == "__main__":
    data = extract_content_from_files(COMBINE_FILE_PATH)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    print(f"Extracted data saved to: {OUTPUT_FILE}")
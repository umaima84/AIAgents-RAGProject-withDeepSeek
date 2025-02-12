import json
import os

BASE_DIR = r"C:\Users\Administrator\Desktop\AI Agents"
EXTRACTED_DATA_FILE = os.path.join(BASE_DIR, "extracted_data.json")
CHUNKED_TEXT_OUTPUT = os.path.join(BASE_DIR, "chunked_text.json")
CHUNKED_CODE_OUTPUT = os.path.join(BASE_DIR, "chunked_code.json")

PYTHON_FILES = [
    os.path.join(BASE_DIR, "RAG-v1_ectract.py"),
    os.path.join(BASE_DIR, "RAG_with_Pytorch-v1_ectract.py"),
    os.path.join(BASE_DIR, "Q8xOtzEyhVCPaXel6SQDiw_ectract.py"),
    os.path.join(BASE_DIR, "prompt-engineering-v1_ectract.py"),
    os.path.join(BASE_DIR, "introduction_to_langchain-v1_ectract.py"),
]

CHUNK_SIZE = 5000
CHUNK_OVERLAP = 200
CODE_LINES = 50
CODE_OVERLAP = 10

def split_text_into_chunks(text, chunk_size=CHUNK_SIZE, overlap=CHUNK_OVERLAP):
    return [text[i:i + chunk_size] for i in range(0, len(text), chunk_size - overlap)]

def process_text_chunking(file_path):
    if not os.path.exists(file_path):
        print(f"Text data file not found: {file_path}")
        return {}

    with open(file_path, "r", encoding="utf-8") as file:
        extracted_data = json.load(file)
    chunked_text_data = {fname: split_text_into_chunks(content) for fname, content in extracted_data.items()}

    with open(CHUNKED_TEXT_OUTPUT, "w", encoding="utf-8") as file:
        json.dump(chunked_text_data, file, indent=4, ensure_ascii=False)
    print(f"Chunked text data saved to {CHUNKED_TEXT_OUTPUT}")
    return chunked_text_data

def load_python_files(filepaths):
    return {
        os.path.basename(filepath): open(filepath, "r", encoding="utf-8").read()
        for filepath in filepaths if os.path.exists(filepath)
    }

def chunk_code(code_text, max_lines=CODE_LINES, overlap=CODE_OVERLAP):
    lines = code_text.split("\n")
    return ["\n".join(lines[i:i + max_lines]) for i in range(0, len(lines), max_lines - overlap)]

def process_code_chunking(file_list):
    extracted_code = load_python_files(file_list)
    chunked_code_data = {fname: chunk_code(code) for fname, code in extracted_code.items()}

    with open(CHUNKED_CODE_OUTPUT, "w", encoding="utf-8") as file:
        json.dump(chunked_code_data, file, indent=4, ensure_ascii=False)
    print(f"Chunked code data saved to {CHUNKED_CODE_OUTPUT}")
    return chunked_code_data

if __name__ == "__main__":
    process_text_chunking(EXTRACTED_DATA_FILE)
    process_code_chunking(PYTHON_FILES)
import json
import os

def extract_code_from_ipynb(filepaths):
    extracted_code = {}
    for filepath in filepaths:
        with open(filepath, 'r', encoding='utf-8') as f:
            notebook = json.load(f)
        code_cells = [cell["source"] for cell in notebook["cells"] if cell["cell_type"] == "code"]
        code_text = "\n\n".join(["".join(cell) for cell in code_cells])
        extracted_code[filepath] = code_text
    return extracted_code

def chunk_code_cells(code_text, max_lines=15, overlap=5):
    chunks = []
    lines = code_text.split("\n")
    for i in range(0, len(lines), max_lines - overlap):
        chunk = "\n".join(lines[i:i + max_lines])
        chunks.append(chunk)
    return chunks

ipynb_files = [
    "RAG-v1.ipynb", 
    "RAG with Pytorch-v1.ipynb", 
    "Q8xOtzEyhVCPaXel6SQDiw.ipynb", 
    "prompt-engineering-v1.ipynb", 
    "introduction to langchain-v1.ipynb"
]

extracted_code = extract_code_from_ipynb(ipynb_files)
chunked_code = {filename: chunk_code_cells(code) for filename, code in extracted_code.items()}

for filename, chunks in chunked_code.items():
    print(f"\n{filename} - Total Chunks: {len(chunks)}")
    print(f"First Chunk:\n{chunks[0]}\n{'='*50}")
    break  
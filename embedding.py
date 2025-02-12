import json
import os
import numpy as np
from transformers import AutoModel, AutoTokenizer
import torch

BASE_DIR = r"C:\Users\Administrator\Desktop\AI Agents"
TEXT_CHUNK_FILE = os.path.join(BASE_DIR, "chunked_text.json")
CODE_CHUNK_FILE = os.path.join(BASE_DIR, "chunked_code.json")
OUTPUT_FILE = os.path.join(BASE_DIR, "embedded_data.json")

MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"
TOKENIZER = AutoTokenizer.from_pretrained(MODEL_NAME)
MODEL = AutoModel.from_pretrained(MODEL_NAME)

def get_embedding(text):
    tokens = TOKENIZER(text, return_tensors="pt", truncation=True, padding=True, max_length=512)
    with torch.no_grad():
        output = MODEL(**tokens)
    return output.last_hidden_state.mean(dim=1).squeeze().numpy()

def load_chunks(file_path):
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return {}

    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)

def process_embeddings(chunked_data):
    return {file_name: [get_embedding(chunk).tolist() for chunk in chunks] for file_name, chunks in chunked_data.items()}

if __name__ == "__main__":
    chunked_text = load_chunks(TEXT_CHUNK_FILE)
    chunked_code = load_chunks(CODE_CHUNK_FILE)
    embedded_text = process_embeddings(chunked_text)
    embedded_code = process_embeddings(chunked_code)

    all_embeddings = {
        "text_embeddings": embedded_text,
        "code_embeddings": embedded_code
    }

    with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
        json.dump(all_embeddings, file, indent=4)
    print(f"Embedding process completed! File saved at: {OUTPUT_FILE}")
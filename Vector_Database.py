import json
import os
import faiss
import numpy as np

BASE_DIR = r"C:\\Users\\Administrator\\Desktop\\AI Agents"
EMBEDDED_DATA_FILE = os.path.join(BASE_DIR, "embedded_data.json")
FAISS_INDEX_FILE = os.path.join(BASE_DIR, "faiss_index.idx")

def load_embedded_data(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Embedded data file not found: {file_path}")
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)

def prepare_data_for_faiss(embedded_data):
    all_vectors = []
    for data_type in ["text_embeddings", "code_embeddings"]:
        for embeddings in embedded_data.get(data_type, {}).values():
            all_vectors.extend(embeddings)

    if not all_vectors:
        raise ValueError("No embeddings found to insert into FAISS index.")
    return np.array(all_vectors, dtype='float32')

def create_faiss_index(vectors, index_file):
    embedding_dim = vectors.shape[1]
    index = faiss.IndexFlatL2(embedding_dim)
    index.add(vectors)
    faiss.write_index(index, index_file)
    print(f"FAISS index created with {index.ntotal} embeddings and saved to: {index_file}")

if __name__ == "__main__":
    embedded_data = load_embedded_data(EMBEDDED_DATA_FILE)
    vectors_to_insert = prepare_data_for_faiss(embedded_data)
    create_faiss_index(vectors_to_insert, FAISS_INDEX_FILE)
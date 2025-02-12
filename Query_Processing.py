import os
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  

BASE_DIR = r"C:\\Users\\Administrator\\Desktop\\AI Agents"
FAISS_INDEX_FILE = os.path.join(BASE_DIR, "faiss_index.idx")
QUERY_RESULTS_FILE = os.path.join(BASE_DIR, "query_results.npy")

def load_faiss_index(index_file):
    if not os.path.exists(index_file):
        raise FileNotFoundError(f"FAISS index file not found: {index_file}")
    return faiss.read_index(index_file)

def load_embedding_model(model_name="sentence-transformers/all-MiniLM-L6-v2"):
    return SentenceTransformer(model_name)

def query_faiss_index(query, index, embedding_model, top_k=2):
    query_embedding = embedding_model.encode([query])[0].astype('float32')
    distances, indices = index.search(np.array([query_embedding]), top_k)
    return indices

if __name__ == "__main__":
    index = load_faiss_index(FAISS_INDEX_FILE)
    embedding_model = load_embedding_model()

    user_query = input("Enter your query: ", flush=True)
    result_indices = query_faiss_index(user_query, index, embedding_model)

    np.save(QUERY_RESULTS_FILE, result_indices)
    print(f"Top matching indices saved for retrieval: {result_indices}")
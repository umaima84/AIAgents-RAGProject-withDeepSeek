import json
import numpy as np

# Paths
chunked_text_file = r"C:\Users\Administrator\Desktop\AI Agents\chunked_text.json"
chunked_code_file = r"C:\Users\Administrator\Desktop\AI Agents\chunked_code.json"
query_results_file = r"C:\Users\Administrator\Desktop\AI Agents\query_results.npy"

# Load original text and code chunks
with open(chunked_text_file, "r", encoding="utf-8") as f:
    chunked_text = json.load(f)

with open(chunked_code_file, "r", encoding="utf-8") as f:
    chunked_code = json.load(f)

# Flatten the chunks for easy index retrieval
all_chunks = []
for chunks in chunked_text.values():
    all_chunks.extend(chunks)
for chunks in chunked_code.values():
    all_chunks.extend(chunks)

# Load query result indices
result_indices = np.load(query_results_file)[0]  # First query result indices

# Retrieve top matching original chunks
retrieved_chunks = [all_chunks[idx] for idx in result_indices]

# Display retrieved content
for i, chunk in enumerate(retrieved_chunks, 1):
    print(f"Result {i}: {chunk}\n")

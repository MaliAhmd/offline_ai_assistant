import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "data", "chunks.txt")
INDEX_PATH = os.path.join(BASE_DIR, "embeddings", "faiss_index")

index = faiss.read_index(INDEX_PATH)

model = SentenceTransformer("all-MiniLM-L6-v2")

with open(DATA_PATH, "r", encoding="utf8") as f:
    docs = f.readlines()


def retrieve(query, k=2):

    q_embed = model.encode([query])

    distances, indices = index.search(np.array(q_embed), k)

    results = []
    filtered_distances = []

    for i in range(len(indices[0])):
        # filter out completely unrelated chunks
        if distances[0][i] < 1.4:
            results.append(docs[indices[0][i]].strip())
            filtered_distances.append(distances[0][i])

    # Ensure distances has at least one element for downstream logic format
    if not filtered_distances:
        filtered_distances = [2.0]

    return results, [filtered_distances]
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "data", "chunks.txt")
INDEX_PATH = os.path.join(BASE_DIR, "embeddings", "faiss_index")

model = SentenceTransformer("all-MiniLM-L6-v2")

docs = []

with open(DATA_PATH, "r", encoding="utf8") as f:

    docs = f.readlines()

embeddings = model.encode(docs)

dim = embeddings.shape[1]

index = faiss.IndexFlatL2(dim)

index.add(np.array(embeddings))

faiss.write_index(index, INDEX_PATH)

print("Embeddings stored")
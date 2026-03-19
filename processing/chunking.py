import os

chunk_size = 500

docs = []

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
clean_dir = os.path.join(BASE_DIR, "data", "cleaned")
chunks_file = os.path.join(BASE_DIR, "data", "chunks.txt")

for file in os.listdir(clean_dir):

    with open(os.path.join(clean_dir, file), "r", encoding="utf8") as f:

        text = f.read()

        # Word-based chunking with overlap
        words = text.split()
        chunk_words = 60 # ~300 chars, fast retrieval and LLM context reading
        overlap_words = 15 # ~75 chars overlap
        
        if len(words) == 0:
            continue
            
        i = 0
        while i < len(words):
            chunk = " ".join(words[i : i + chunk_words])
            docs.append(chunk)
            if i + chunk_words >= len(words):
                break
            i += (chunk_words - overlap_words)

with open(chunks_file, "w", encoding="utf8") as f:

    for d in docs:
        f.write(d + "\n")

print("Chunking complete")
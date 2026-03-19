from fastapi import FastAPI
from rag.retriever import retrieve
from llama_cpp import Llama

app = FastAPI()

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "models", "Meta-Llama-3-8B-Instruct-Q4_K_M.gguf")

llm = Llama(
    model_path=MODEL_PATH,
    n_ctx=4096
)

def build_prompt(context, question):

    prompt = f"""
You are an assistant for Nidrip Central Electronics.

Answer ONLY using the context below.

Context:
{context}

Question:
{question}

Answer:
"""

    return prompt


@app.post("/chat")
def chat(query: str):

    docs, distances = retrieve(query)

    context = "\n".join(docs)

    prompt = build_prompt(context, query)

    response = llm(prompt, max_tokens=300)

    answer = response["choices"][0]["text"]

    if distances[0][0] > 1.5:

        return {
            "response": "I'm not confident in this answer. Please contact human support."
        }

    return {"response": answer}
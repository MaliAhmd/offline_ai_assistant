import os
import sys
from llama_cpp import Llama

# Add current directory to path so it can import rag
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from rag.retriever import retrieve

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "models", "Meta-Llama-3-8B-Instruct-Q4_K_M.gguf")

print("Loading Offline AI Model... (This might take a moment)")
llm = Llama(
    model_path=MODEL_PATH,
    n_ctx=4096,
    verbose=False  # Hide llama.cpp debug output
)

def build_prompt(context, question):
    prompt = f"""You are an assistant for Nidrip Central Electronics.

Answer ONLY using the context below.

Context:
{context}

Question:
{question}

Answer:"""
    return prompt

print("\n==============================================")
print("     Nidrip Central Electronics Terminal AI     ")
print("==============================================\n")
print("Type 'exit' or 'quit' to stop.\n")

while True:
    try:
        query = input("You: ")
        if query.strip().lower() in ['exit', 'quit']:
            break
            
        if not query.strip():
            continue
            
        print("Thinking...")
        docs, distances = retrieve(query)
        context = "\n".join(docs)
        prompt = build_prompt(context, query)
        
        response = llm(prompt, max_tokens=300)
        answer = response["choices"][0]["text"].strip()
        
        if distances[0][0] > 1.5:
            print(f"\nAssistant: {answer}")
            print("\n[Warning: I'm not entirely confident in this answer based on the context. Please contact human support if needed.]\n")
        else:
            print(f"\nAssistant: {answer}\n")
            
    except KeyboardInterrupt:
        break
    except Exception as e:
        print(f"\nAn error occurred: {str(e)}\n")

print("\nGoodbye!")

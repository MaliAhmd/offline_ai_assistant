# 🧠 Offline AI Assistant (RAG Chatbot) – Windows

A fully **offline AI chatbot system** built using Python, FastAPI, and a local LLM (Llama 3).
The assistant answers queries strictly based on a custom knowledge base scraped from a website.

---

## 🚀 Features

* ✅ Fully **offline** (no cloud dependency)
* ✅ Uses **Llama 3 (local GGUF model)**
* ✅ Implements **RAG (Retrieval-Augmented Generation)**
* ✅ Fast **vector search using FAISS**
* ✅ Answers only from provided data
* ✅ Built-in **hallucination control (confidence check)**
* ✅ Local API via FastAPI

---

## 🏗️ Project Structure

```
Offline_ai_assistant/
│
├── api/                # FastAPI backend
│   └── main.py
│
├── scraper/            # Website scraping
│   └── scraper.py
│
├── processing/         # Data cleaning & chunking
│   ├── clean_data.py
│   └── chunking.py
│
├── rag/                # Embeddings & retrieval
│   ├── embed.py
│   └── retriever.py
│
├── data/
│   ├── raw/            # Raw scraped data
│   └── cleaned/        # Cleaned data
│
├── embeddings/         # FAISS index
│
├── models/             # Llama model (GGUF)
│
├── requirements.txt
└── run.bat
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone Repository

```
git clone <your-repo-url>
cd Offline_ai_assistant
```

---

### 2️⃣ Create Virtual Environment

```
python -m venv myenv
myenv\Scripts\activate
```

---

### 3️⃣ Install Dependencies

```
pip install -r requirements.txt
```

---

### 4️⃣ Download Model

Download **Llama 3 GGUF model** and place inside:

```
models/
```

Example:

```
models/llama3.gguf
```

---

## 📊 Data Pipeline (Run Once)

### Step 1 – Scrape Website

```
cd scraper
python scraper.py
```

---

### Step 2 – Clean Data

```
cd ../processing
python clean_data.py
```

---

### Step 3 – Chunk Data

```
python chunking.py
```

---

### Step 4 – Generate Embeddings

```
cd ../rag
python embed.py
```

---

## ▶️ Run the Application

From project root:

```
uvicorn api.main:app --reload
```

Open:

```
http://127.0.0.1:8000/docs
```

---

## 💬 API Usage

### Endpoint

```
POST /chat
```

### Example Request

```json
{
  "query": "What services does the company provide?"
}
```

### Example Response

```json
{
  "response": "The company provides electronic appliances and services..."
}
```

---

## 🧠 How It Works

1. Website data is scraped and cleaned
2. Text is split into chunks
3. Chunks are converted into embeddings
4. Stored in FAISS vector database
5. User query is matched with relevant chunks
6. Llama 3 generates answer using retrieved context

---

## 🛡️ Safety Feature

If the system is not confident:

```
"I'm not confident in this answer. Please contact human support."
```

---

## 💻 Requirements

* Python 3.10+
* 16GB RAM (minimum)
* Windows OS

---

## 📦 Deployment

* Fully local deployment
* Delivered as ZIP file
* No internet required after setup

---

## 🔮 Future Improvements

* Chat UI (frontend)
* Full website crawler
* Better ranking (reranking)
* Multi-language support

---

## 👨‍💻 Author

Muhammad Ali Ahmad
Software Engineer

---

## 📜 License

This project is for educational and client delivery purposes.

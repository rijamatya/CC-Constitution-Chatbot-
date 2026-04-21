# Constitution RAG Chatbot (FAISS + LLM)

## Project Overview

This project is a domain-specific chatbot that answers questions related to the Constitution of Nepal using a Retrieval-Augmented Generation (RAG) approach. The system retrieves relevant information from a constitution PDF and generates accurate responses using a Large Language Model (LLM).

The chatbot ensures that responses are grounded in the provided document rather than relying only on pretrained model knowledge.

---

## Objectives

- Build a chatbot using RAG architecture
- Extract and process text from a PDF document
- Implement vector search using FAISS
- Generate responses using a Large Language Model
- Restrict the chatbot to domain-specific (constitution-based) queries

---

## Technologies Used

- Python
- Streamlit (for user interface)
- SentenceTransformers (for embeddings)
- FAISS (for vector similarity search)
- Ollama (LLaMA3) or Hugging Face Transformers (LLM)
- PyPDF (for PDF text extraction)

---

## How It Works (RAG Pipeline)

The system follows a Retrieval-Augmented Generation pipeline:

1. Load Constitution PDF document
2. Split text into smaller chunks
3. Convert text chunks into embeddings
4. Store embeddings in FAISS vector database
5. Accept user query
6. Retrieve most relevant text chunks using similarity search
7. Pass retrieved context to the LLM
8. Generate and return final answer

---

## Architecture

User Query  
↓  
Embedding Generation  
↓  
FAISS Vector Search  
↓  
Relevant Document Chunks  
↓  
LLM (LLaMA3 / Hugging Face Model)  
↓  
Final Answer

---

## Features

- Domain-specific question answering system
- Semantic search using FAISS vector database
- Context-aware response generation
- PDF-based knowledge extraction
- Streamlit-based interactive chatbot interface
- Restriction to constitution-related queries only

---

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/constitution-rag-chatbot.git
cd constitution-rag-chatbot

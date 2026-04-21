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

a. Python
b. Streamlit (for UI)
c. SentenceTransformers (for embeddings)
d. FAISS (for vector search)
e. Ollama (LLaMA3) (for response generation)
f. PyPDF (for extracting text from PDF)
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



## Features

- Domain-specific question answering system
- Semantic search using FAISS vector database
- Context-aware response generation
- PDF-based knowledge extraction
- Streamlit-based interactive chatbot interface
- Restriction to constitution-related queries only

---


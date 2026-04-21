Constitution RAG Chatbot (FAISS + LLM)

Project Overview
This project is a domain-specific chatbot that answers questions related to the Constitution of Nepal using a Retrieval-Augmented Generation (RAG) approach. The system retrieves relevant information from a constitution PDF and generates accurate responses using a Large Language Model.

Objectives
a. Build a chatbot using RAG architecture
b. Extract knowledge from a PDF document
c. Implement vector search using FAISS
d. Generate responses using an LLM
e. Restrict chatbot to domain-specific queries

Technologies Used
a. Python
b. Streamlit (for UI)
c. SentenceTransformers (for embeddings)
d. FAISS (for vector search)
e. Ollama (LLaMA3) (for response generation)
f. PyPDF (for extracting text from PDF)

How It Works (RAG Pipeline)
-Load Constitution PDF
-Split text into chunks
-Convert chunks into embeddings
-Store embeddings in FAISS index
-User asks a question
-Retrieve most relevant chunks
-LLM generates answer using context

Author
Rij Amatya

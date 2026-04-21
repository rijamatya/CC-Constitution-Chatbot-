import streamlit as st
from pypdf import PdfReader
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import ollama

# PAGE CONFIG
st.set_page_config(page_title="Constitution RAG Chatbot")
st.title("Constitution RAG Chatbot (FAISS + LLM)")

# LOAD PDF 
@st.cache_data
def load_pdf(file_path):
    reader = PdfReader(file_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

pdf_file = "constitution.pdf"  
full_text = load_pdf(pdf_file)

# SPLIT TEXT INTO CHUNKS 
def split_text(text, chunk_size=1000):
    chunks = []
    for i in range(0, len(text), chunk_size):
        chunks.append(text[i:i+chunk_size])
    return chunks

chunks = split_text(full_text)

# EMBEDDINGS 
@st.cache_resource
def load_embedder():
    return SentenceTransformer('all-MiniLM-L6-v2')

embedder = load_embedder()

@st.cache_data
def create_embeddings(chunks):
    return embedder.encode(chunks)

chunk_embeddings = create_embeddings(chunks)

# FAISS INDEX 
embedding_dim = chunk_embeddings.shape[1]
index = faiss.IndexFlatL2(embedding_dim)
index.add(np.array(chunk_embeddings).astype('float32'))

# SESSION STATE 
if "messages" not in st.session_state:
    st.session_state.messages = []

#  DISPLAY CHAT HISTORY 
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

#  RETRIEVAL FUNCTION 
def retrieve_context(query, k=5):
    query_embedding = embedder.encode([query]).astype('float32')
    D, I = index.search(query_embedding, k)
    context = ""
    for idx in I[0]:
        context += chunks[idx] + "\n\n"
    return context

# USER INPUT
if prompt := st.chat_input("Ask a question about the constitution"):
    # Save user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Retrieve relevant chunks
    retrieved_context = retrieve_context(prompt, k=3)

    # Build system prompt for LLM
    system_prompt = f"""
You are a legal assistant specialized in the Constitution of Nepal.

Your behavior must follow these rules:

1. If the user greets you (e.g., says "hi", "hello", "hey"), respond politely and introduce yourself as a legal assistant for the Constitution of Nepal.

2. If the question is related to the Constitution of Nepal, answer it using ONLY the provided context.

3. If the question is unrelated (e.g., movies, celebrities, general knowledge like "Spiderman"), respond EXACTLY with:
"I am a legal assistant that can only provide information related to the Constitution of Nepal."

4. If the answer is not found in the context, respond:
"Not found in the constitution."

5. Keep answers clear, complete, and simple.

Context:
{retrieved_context}
"""

    # Limit chat history to last few messages
    MAX_HISTORY = 4
    recent_messages = st.session_state.messages[-MAX_HISTORY:]

    # Generate response using Ollama LLaMA3 (or another model)
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""

        stream = ollama.chat(
            model="llama3",  # You can change model if needed
            messages=[{"role": "system", "content": system_prompt}, *recent_messages],
            stream=True,
            options={"num_predict": 400, "temperature": 0.3}
        )

        for chunk in stream:
            full_response += chunk["message"]["content"]
            message_placeholder.markdown(full_response)

        # Save assistant response
        st.session_state.messages.append({"role": "assistant", "content": full_response})
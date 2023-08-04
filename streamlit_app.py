import tempfile

import streamlit as st
from langchain.chains import RetrievalQA
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Chroma

from vertex_ai.vertex_ai import gcp_chat, gcp_embeddings, gcp_llm


def generate_response(uploaded_file, query_text):
    # Load document if file is uploaded
    if uploaded_file is not None:
        # Check if document is PDF
        if uploaded_file.type == "application/pdf":
            with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
                tmp.write(uploaded_file.getvalue())
                tmp_location = tmp.name

            loader = PyPDFLoader(tmp_location)
            texts = loader.load_and_split()
        # Otherwise, read as text
        else:
            documents = [uploaded_file.read().decode()]
            # Split documents into chunks
            text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
            texts = text_splitter.create_documents(documents)
        # Select embeddings
        embeddings = gcp_embeddings
        # Create a vectorstore from documents
        db = Chroma.from_documents(texts, embeddings)
        # Create retriever interface
        retriever = db.as_retriever()
        # Create QA chain
        qa = RetrievalQA.from_chain_type(
            llm=gcp_chat, chain_type="stuff", retriever=retriever
        )
        return qa.run(query_text)


# Page title
st.set_page_config(page_title="🦜🔗 Ask the Doc App")
st.title("🦜🔗 Ask the Doc App")

# File upload
uploaded_file = st.file_uploader(
    "Upload a document",
    type=["txt", "pdf", "html", "md", "csv", "json", "xml"],
)
# Query text
query_text = st.text_input(
    "Enter your question:",
    placeholder="Please provide a short summary.",
    disabled=not uploaded_file,
)

# Form input and query
result = []
with st.form("myform", clear_on_submit=True):
    submitted = st.form_submit_button(
        "Submit", disabled=not (uploaded_file and query_text)
    )
    if submitted:
        with st.spinner("Calculating..."):
            response = generate_response(uploaded_file, query_text)
            result.append(response)

if len(result):
    st.info(response)

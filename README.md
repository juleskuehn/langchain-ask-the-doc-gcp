# 🦜🔗 LangChain - Ask the Doc

Build a Document Question Answering app using LangChain and Streamlit.

Modified to use Google Cloud Platform Vertex AI LLMs and embeddings.

## Setup

```bash
pip install -r requirements.txt
gcloud auth application-default login
```

## Run the app

```bash
streamlit run .\streamlit_app.py
```

Once the app is loaded, upload a file, type a question in the text box, Submit, and wait for a generated response.

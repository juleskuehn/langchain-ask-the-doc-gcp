# 🦜🔗 LangChain - Ask the Doc

Build a Document Question Answering app using LangChain and Streamlit.

Modified to use Google Cloud Platform Vertex AI LLMs and embeddings.

## Setup

Requires Python 3.10+ and the Google Cloud CLI ([follow the instructions here](https://cloud.google.com/sdk/docs/install)).

Recommended to create an activate a venv for the project, i.e.
```bash
python -m venv venv
source venv/bin/activate
```

Install the requirements and authorize to GCP.
```bash
pip install -r requirements.txt
gcloud auth application-default login
```

## Run the app

```bash
streamlit run .\streamlit_app.py
```

Once the app is loaded, upload a file, type a question in the text box, Submit, and wait for a generated response.

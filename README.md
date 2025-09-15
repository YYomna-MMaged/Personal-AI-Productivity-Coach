# 🤖 Personal AI Productivity Coach

An AI-powered productivity assistant that helps you analyze daily reports, organize tasks, and improve habits using Large Language Models (LLMs).
It provides actionable suggestions, daily performance scoring, and interactive dashboards via Streamlit.
---

## 🚀 Features
- Analyze free-text daily reports and generate structured feedback.
- Organize and prioritize tasks intelligently.
- Evaluate productivity with a custom scoring system (sleep, habits, tasks completed, punctuality).
- Interactive Streamlit interface for easy user interaction.
- Optional Telegram integration for automated report notifications.

---

## 📂 Project Structure

```bash
personal-ai-productivity-coach/
├── scr/                       # Core backend scripts and modules
│   ├── server_model.py         # Functions to analyze daily reports and tasks using LLMs
│   ├── retriever.py            # Functions to retrieve information from the knowledge base
│   ├── analysis.py             # Analysis utilities (e.g., scoring, insights extraction)
│   ├── embeddings.py           # Handles embeddings generation for knowledge and tasks
│   ├── kb_generator.py         # Generates or updates the knowledge base
│   ├── llm_prompts.py          # Prompts templates for guiding LLM behavior
│
├── run on kaggle only/         # Kaggle-specific notebooks and experiments
│   ├── model-point.ipynb       # Notebook for testing/loading models on Kaggle environment
│
├── kb/                         # Knowledge base storage
│   ├── kn_chunks.json          # Preprocessed knowledge chunks used by the system
│
├── tests/                      # Testing scripts and notebooks
│   ├── embedding_test.ipynb    # Notebook for testing embeddings generation
│   ├── embeddings_faiss.py     # Script for managing FAISS vector store
│   ├── kb_vector.index         # FAISS vector index file
│   ├── kb_vector.meta.json     # Metadata for FAISS vector store
│
├── app.py                      # Main Streamlit application for user interaction
├── requirements.txt            # Python dependencies and package versions
├── README.md                   # Project documentation and usage instructions
```
---
## 🛠️ Installation

1. Clone this repository:
```bash
   git clone https://github.com/YYomna-MMaged/Personal-AI-Productivity-Coach.git
    cd Personal-AI-Productivity-Coach
```
2. Create a virtual environment and activate it:
```bash
python -m venv .venv
source .venv/bin/activate   # Linux/Mac
.venv\Scripts\activate      # Windows
```
3. Install dependencies:
```bash
pip install -r requirements.txt
``` 
---
## 🌐 Deployment (Streamlit Cloud)
1. Push your code to GitHub.  
2. Go to [Streamlit Cloud](https://share.streamlit.io/).  
3. Deploy the repo and set:  
   - **Main file path:** `app.py`  
4. Your app will be live online 🎉  

---

## 📦 Requirements
Main dependencies:
- `streamlit`  
- `transformers`  
- `torch`  
- `huggingface-hub`  

(Full list in `requirements.txt`) 
import json
import chromadb
from chromadb.config import Settings
from chromadb.utils import embedding_functions
from sentence_transformers import SentenceTransformer

import os
from dotenv import load_dotenv
load_dotenv()
token = os.getenv("HUGGINGFACE_HUB_TOKEN")
os.environ['HUGGINGFACE_HUB_TOKEN'] = token
# print(os.getenv("HUGGINGFACE_HUB_TOKEN"))

# Embedding function
embedding_fun = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name = "intfloat/multilingual-e5-base",
    normalize_embeddings = True
)

client = chromadb.PersistentClient(path="./kb_chroma")

#Creating vector database for knowledge base
def kb_vectors(kb_chunks , collection_name = "kb_vectors",client = client, embedding_fun = embedding_fun):
    with open(kb_chunks, 'r', encoding = 'utf-8') as file:
        chunks = json.load(file)

    texts = [chunk['text'] for chunk in chunks]
    ids = [chunk['id'] for chunk in chunks]
    metadatas = [{"source": chunk.get('source', 'unknoWn')} for chunk in chunks]

    if collection_name in [c.name for c in client.list_collections()]:
        collection = client.get_collection(collection_name,embedding_function = embedding_fun)
    else:
        collection = client.create_collection(name = collection_name, embedding_function = embedding_fun) 
    
    collection.add(ids=ids, documents = texts, metadatas = metadatas)

    return collection_name


if __name__ == "__main__":
    kb_chunks = '../kb/kb_chunks.json'
    collection_name = kb_vectors(kb_chunks)
    print(f"✅ ChromaDB collection '{collection_name}' built and persisted!")
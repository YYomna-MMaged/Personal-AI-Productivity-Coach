import os
import json
import numpy as np
from sentence_transformers import SentenceTransformer
import faiss

model = SentenceTransformer("intfloat/multilingual-e5-base")

#Embedding texts in chunks
def embed_chunks(texts, model):
    embeddings = model.encode(texts, 
                             show_progress_bar = True,
                             normlize_embeddings = True)
    return embeddings

#Creating vector database for knowledge base
def kb_vectors(kb_chunks , model = model):
    with open(kb_chunks, 'r', encoding = 'utf-8') as file:
        chunks = json.load(file)

    texts = [chunk['text'] for chunk in chunks]
    ids = [chunk['id'] for chunk in chunks]

    embeddings = embed_chunks(texts, model)

    dim = embeddings.shape[1]
    index = faiss.IndexFlatIP(dim)
    index.add(embeddings)

    index_file = 'kb_vector.index'
    meta_file = 'kb_vector.meta.json'

    faiss.write_index(index, index_file)

    with open(meta_file, 'w', encoding = 'utf-8') as file:
        json.dump(ids, file, ensure_ascii = False, indent = 2)

    return index_file, meta_file


if __name__ == "__main__":
    kb_chunks = '../kb/kb_chunks.json'
    index_file, meta_file = kb_vectors(kb_chunks)
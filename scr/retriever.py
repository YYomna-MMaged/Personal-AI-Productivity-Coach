import chromadb
from chromadb.utils import embedding_functions

import os
from dotenv import load_dotenv
load_dotenv()
token = os.getenv("HUGGINGFACE_HUB_TOKEN")
os.environ['HUGGINGFACE_HUB_TOKEN'] = token
# print(os.getenv("HUGGINGFACE_HUB_TOKEN"))

embedding_fun = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name = "intfloat/multilingual-e5-base",
    normalize_embeddings = True
)

client = chromadb.PersistentClient(path="./kb_chroma")

def get_collection(collection_name = 'kb_vectors'):
    if collection_name in [c.name for c in client.list_collections()]:
        collection = client.get_collection(name = collection_name, embedding_function = embedding_fun)
        return collection
    else:
        raise ValueError(f"Collection {collection_name} doesn`t exist.")


def retrieve(query, collection, n_results = 5):
    query_embedding = embedding_fun([query])[0]

    results = collection.query(
        query_embeddings = [query_embedding],
        n_results = n_results
    )

    retrieved = []
    for doc, meta in zip(results['documents'][0], results['metadatas'][0]):
        retrieved.append({'text' : doc, 'source' : meta.get('source', 'unkown')})

    return retrieved

if __name__ == "__main__":
    coll = get_collection()
    query = "improve my time managment skills"
    results = retrieve(query, collection=coll)
    for i, r in enumerate(results):
        print(f"{i+1}. Source: {r['source']}\n   Text: {r['text']}\n")
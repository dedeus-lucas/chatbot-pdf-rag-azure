# src/vector_store.py

import os
import pickle
import numpy as np
import faiss

from text_chunker import chunk_documents
from pdf_loader import load_all_pdfs
from openai import OpenAI


# Diretórios
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUT_DIR = os.path.join(BASE_DIR, "outputs")

os.makedirs(OUTPUT_DIR, exist_ok=True)


# Inicializar cliente OpenAI
client = OpenAI()


EMBEDDING_MODEL = "text-embedding-3-small"


def get_embedding(text: str) -> np.ndarray:
    """
    Gera embedding para um texto
    """

    response = client.embeddings.create(
        model=EMBEDDING_MODEL,
        input=text
    )

    embedding = response.data[0].embedding

    return np.array(embedding, dtype="float32")


def build_vector_store():

    print("Loading PDFs...")
    documents = load_all_pdfs()

    print("Chunking documents...")
    chunks = chunk_documents(documents)

    print(f"Total chunks: {len(chunks)}")

    embeddings = []
    metadata = []

    print("Generating embeddings...")

    for chunk in chunks:

        emb = get_embedding(chunk["content"])

        embeddings.append(emb)
        metadata.append(chunk)

    embeddings_np = np.vstack(embeddings)

    print("Building FAISS index...")

    dimension = embeddings_np.shape[1]

    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings_np)

    print(f"Total vectors indexed: {index.ntotal}")

    # salvar index
    faiss.write_index(index, os.path.join(OUTPUT_DIR, "vector_index.faiss"))

    # salvar metadata
    with open(os.path.join(OUTPUT_DIR, "metadata.pkl"), "wb") as f:
        pickle.dump(metadata, f)

    print("Vector store saved successfully.")


if __name__ == "__main__":

    build_vector_store()

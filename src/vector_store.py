import os
import pickle
import numpy as np
import faiss

from dotenv import load_dotenv
from openai import OpenAI

from text_chunker import chunk_documents
from pdf_loader import load_all_pdfs


# carregar variáveis do .env
load_dotenv()


# Diretórios
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUT_DIR = os.path.join(BASE_DIR, "outputs")

os.makedirs(OUTPUT_DIR, exist_ok=True)


# Variáveis Azure OpenAI
AZURE_OPENAI_API_KEY = os.getenv("AZURE_OPENAI_API_KEY")
AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
AZURE_OPENAI_EMBEDDING_DEPLOYMENT = os.getenv("AZURE_OPENAI_EMBEDDING_DEPLOYMENT")


# Inicializar cliente Azure OpenAI
client = OpenAI(
    api_key=AZURE_OPENAI_API_KEY,
    base_url=f"{AZURE_OPENAI_ENDPOINT}openai/deployments/{AZURE_OPENAI_EMBEDDING_DEPLOYMENT}/"
)


def get_embedding(text: str) -> np.ndarray:

    response = client.embeddings.create(
        model=AZURE_OPENAI_EMBEDDING_DEPLOYMENT,
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

    faiss.write_index(index, os.path.join(OUTPUT_DIR, "vector_index.faiss"))

    with open(os.path.join(OUTPUT_DIR, "metadata.pkl"), "wb") as f:
        pickle.dump(metadata, f)

    print("Vector store saved successfully.")


if __name__ == "__main__":

    build_vector_store()

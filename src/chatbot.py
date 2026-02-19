import os
import pickle
import numpy as np
import faiss

from dotenv import load_dotenv
from openai import AzureOpenAI


load_dotenv()


# Cliente Azure OpenAI
client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version="2024-02-15-preview",
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
)


CHAT_DEPLOYMENT = os.getenv("AZURE_OPENAI_CHAT_DEPLOYMENT")


# Diretórios
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUT_DIR = os.path.join(BASE_DIR, "outputs")


# carregar index
index = faiss.read_index(
    os.path.join(OUTPUT_DIR, "vector_index.faiss")
)

# carregar metadata
with open(
    os.path.join(OUTPUT_DIR, "metadata.pkl"),
    "rb"
) as f:
    metadata = pickle.load(f)


def get_embedding(text):

    response = client.embeddings.create(
        model=os.getenv("AZURE_OPENAI_EMBEDDING_DEPLOYMENT"),
        input=text
    )

    return np.array(
        response.data[0].embedding,
        dtype="float32"
    )


def search(query, k=3):

    query_embedding = get_embedding(query)

    query_embedding = np.expand_dims(query_embedding, axis=0)

    distances, indices = index.search(query_embedding, k)

    results = []

    for idx in indices[0]:
        results.append(metadata[idx]["content"])

    return results


def ask(question):

    contexts = search(question)

    context_text = "\n\n".join(contexts)

    prompt = f"""
Use o contexto abaixo para responder a pergunta.

Contexto:
{context_text}

Pergunta:
{question}

Resposta:
"""

    response = client.chat.completions.create(
        model=CHAT_DEPLOYMENT,
        messages=[
            {"role": "system", "content": "Você é um assistente que responde com base em documentos."},
            {"role": "user", "content": prompt}
        ],
        temperature=0
    )

    return response.choices[0].message.content


if __name__ == "__main__":

    print("Chatbot RAG iniciado. Digite 'sair' para encerrar.\n")

    while True:

        question = input("Pergunta: ")

        if question.lower() == "sair":
            break

        answer = ask(question)

        print("\nResposta:")
        print(answer)
        print("\n" + "-"*50 + "\n")

from typing import List, Dict

CHUNK_SIZE = 500
CHUNK_OVERLAP = 50


def split_text(text: str, chunk_size: int = CHUNK_SIZE, overlap: int = CHUNK_OVERLAP) -> List[str]:
    """
    Divide texto em chunks com overlap para preservar contexto.
    """

    chunks = []
    start = 0
    text_length = len(text)

    while start < text_length:
        end = start + chunk_size

        chunk = text[start:end]
        chunks.append(chunk)

        start += chunk_size - overlap

    return chunks


def chunk_documents(documents: Dict[str, str]) -> List[Dict]:
    """
    Recebe dict {filename: text}
    Retorna lista estruturada de chunks
    """

    chunked_docs = []

    for filename, text in documents.items():

        chunks = split_text(text)

        for i, chunk in enumerate(chunks):
            chunked_docs.append({
                "source": filename,
                "chunk_id": i,
                "content": chunk
            })

    return chunked_docs


if __name__ == "__main__":

    from pdf_loader import load_all_pdfs

    docs = load_all_pdfs()

    chunked = chunk_documents(docs)

    print(f"\nTotal chunks created: {len(chunked)}\n")

    print("Example chunk:\n")
    print(chunked[0])

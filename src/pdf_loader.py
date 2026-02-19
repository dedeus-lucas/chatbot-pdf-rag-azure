import os
from PyPDF2 import PdfReader

# Caminho absoluto até a raiz do projeto
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Caminho absoluto até a pasta inputs
INPUTS_DIR = os.path.join(PROJECT_ROOT, "inputs")

def load_pdf(pdf_path):
    reader = PdfReader(pdf_path)
    text = ""

    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"

    return text

def load_all_pdfs():
    pdf_texts = {}

    print(f"Searching PDFs in: {INPUTS_DIR}")

    if not os.path.exists(INPUTS_DIR):
        raise Exception(f"Inputs folder not found at: {INPUTS_DIR}")

    for filename in os.listdir(INPUTS_DIR):
        if filename.lower().endswith(".pdf"):
            full_path = os.path.join(INPUTS_DIR, filename)
            print(f"Loading: {filename}")
            pdf_texts[filename] = load_pdf(full_path)

    return pdf_texts


if __name__ == "__main__":
    texts = load_all_pdfs()

    print("\nPDFs loaded successfully.\n")

    for name, content in texts.items():
        print(f"--- {name} ---")
        print(content[:300])
        print("\n")

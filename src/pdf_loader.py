import os
from PyPDF2 import PdfReader

# Caminho absoluto baseado na localização deste arquivo
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INPUTS_DIR = os.path.join(BASE_DIR, "inputs")

def load_pdf(path):
    reader = PdfReader(path)
    text = ""

    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"

    return text

def load_all_pdfs():
    pdf_texts = {}

    if not os.path.exists(INPUTS_DIR):
        raise FileNotFoundError(f"Inputs folder not found: {INPUTS_DIR}")

    for filename in os.listdir(INPUTS_DIR):
        if filename.endswith(".pdf"):
            full_path = os.path.join(INPUTS_DIR, filename)
            print(f"Loading: {filename}")
            pdf_texts[filename] = load_pdf(full_path)

    return pdf_texts

if __name__ == "__main__":
    all_texts = load_all_pdfs()

    for fname, text in all_texts.items():
        print(f"\n--- {fname} ---")
        print(text[:500])

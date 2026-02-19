# Chatbot RAG com Azure OpenAI e FAISS para Consulta Inteligente de PDFs
O projeto não possui um nome específico, resolvi explicá-lo

## 📖 Descrição do Projeto

Este projeto implementa um chatbot inteligente baseado na arquitetura RAG (Retrieval-Augmented Generation), capaz de responder perguntas com base no conteúdo de documentos PDF.

A solução utiliza Azure OpenAI para geração de embeddings e respostas contextuais, FAISS para indexação vetorial de alta performance e FastAPI para exposição de uma API REST profissional.

O sistema funciona em quatro etapas principais:

1. Ingestão de documentos PDF
2. Segmentação dos textos em chunks semânticos
3. Geração de embeddings utilizando Azure OpenAI
4. Recuperação vetorial e geração de respostas contextuais com modelo GPT

Ao receber uma pergunta, o sistema realiza uma busca semântica nos documentos indexados e utiliza o modelo de linguagem para gerar uma resposta precisa e fundamentada no conteúdo fornecido.

Este projeto demonstra competências práticas em:

- Inteligência Artificial Generativa
- Arquitetura RAG
- Azure OpenAI Service
- Embeddings e busca vetorial
- Engenharia de prompts
- Construção de APIs com FastAPI
- Processamento de documentos PDF
- Integração com serviços em nuvem

Este projeto foi desenvolvido como parte do Microsoft Certification Challenge (DP-100), com foco na construção de soluções reais de Machine Learning e IA no Azure.

O resultado é um sistema escalável, modular e pronto para aplicações reais como:

- Assistentes acadêmicos
- Sistemas de suporte técnico
- Chatbots corporativos
- Sistemas de consulta documental
- Ferramentas de auxílio para pesquisa científica

## 🏗️ Arquitetura do Sistema

O sistema implementa um pipeline de Retrieval-Augmented Generation (RAG) utilizando Azure OpenAI para responder perguntas com base em documentos PDF.

Fluxo de funcionamento:

1. Ingestão de documentos
   - PDFs são carregados e convertidos em texto
   - O texto é dividido em chunks menores

2. Geração de embeddings
   - Cada chunk é convertido em vetor usando Azure OpenAI Embeddings
   - Os vetores são armazenados em um banco vetorial (ChromaDB)

3. Consulta do usuário
   - A pergunta do usuário é convertida em embedding
   - O sistema busca os chunks mais relevantes no banco vetorial

4. Geração da resposta
   - Os chunks relevantes são enviados como contexto para o modelo GPT-4o
   - O modelo gera uma resposta baseada exclusivamente no conteúdo recuperado

Arquitetura simplificada:

User → FastAPI → Embedding → Vector Store → Context Retrieval → GPT-4o → Response

## 🧰 Stack Tecnológica

Este projeto foi construído utilizando tecnologias modernas para implementação de sistemas de IA baseados em Retrieval-Augmented Generation (RAG).

### ☁️ Cloud & IA

- Azure OpenAI Service  
  - Modelo de geração: GPT-4o  
  - Modelo de embeddings: text-embedding-3-large  

### 🧠 Processamento e IA

- OpenAI Python SDK  
- ChromaDB (Vector Database)  
- Sentence chunking e embedding pipeline  

### ⚙️ Backend

- Python 3.10+
- FastAPI
- Uvicorn

### 📄 Processamento de documentos

- PyPDF
- Pipeline de ingestão e segmentação de texto

### 🔧 Ferramentas auxiliares

- python-dotenv (gerenciamento de variáveis de ambiente)
- Git e GitHub (versionamento)
- Ambiente virtual Python (venv)

### 🧪 Ambiente de desenvolvimento

- Visual Studio Code
- Windows 11

## 📁 Estrutura do Projeto

A estrutura do projeto segue boas práticas de organização, separando responsabilidades entre ingestão de dados, lógica de IA, API e armazenamento vetorial.

```
chatbot-pdf-rag-azure/
│
├── inputs/                     # PDFs utilizados como base de conhecimento
│   ├── redes_fundamentos.pdf
│   └── redes_topologias_protocolos.pdf
│
├── outputs/                    # Vector store persistido
│   ├── vector_index.faiss
│   └── metadata.pkl
│
├── src/                        # Código-fonte principal
│   ├── __init__.py             # Inicializa o módulo Python
│   ├── api.py                  # API REST com FastAPI
│   ├── chatbot.py              # Lógica principal do chatbot (RAG)
│   ├── pdf_loader.py           # Carregamento de PDFs
│   ├── text_chunker.py         # Divisão de texto em chunks
│   └── vector_store.py         # Criação e persistência do índice vetorial
│
├── notebooks/                  # Experimentos e testes (vazia)
│
├── docs/                       # Documentação técnica (vazia pela simplicidade do projeto)
│
├── requirements.txt            # Dependências do projeto
│
├── .env                        # Variáveis de ambiente (não versionado)
├── .gitignore                  # Arquivos ignorados pelo Git
└── README.md                   # Documentação principal do projeto
```
### 📌 Descrição dos componentes

- src/api.py  
  Responsável por expor o chatbot através de uma API REST usando FastAPI.

- src/chatbot.py  
  Implementa o pipeline RAG completo:
  - Recebe perguntas
  - Busca documentos relevantes no vector store
  - Envia contexto para o modelo GPT-4o
  - Retorna resposta contextualizada

- src/create_vector_store.py  
  Script responsável por:
  - Ler arquivos PDF
  - Dividir em chunks
  - Gerar embeddings
  - Armazenar no ChromaDB

- chroma_db/  
  Contém o banco vetorial persistente, permitindo reutilização sem necessidade de reprocessar os documentos.

- data/  
  Diretório contendo os documentos fonte utilizados como base de conhecimento.

- .env  
  Armazena credenciais sensíveis e configurações do Azure OpenAI.

## 🚀 Como executar localmente

### 1. Clonar o repositório

git clone https://github.com/SEU-USUARIO/chatbot-pdf-rag-azure.git

cd chatbot-pdf-rag-azure


### 2. Criar e ativar ambiente virtual

Windows:

python -m venv venv
venv\Scripts\activate

Linux / Mac:

python3 -m venv venv
source venv/bin/activate


### 3. Instalar dependências

pip install -r requirements.txt


### 4. Configurar variáveis de ambiente

Criar arquivo `.env` na raiz do projeto:

AZURE_OPENAI_API_KEY=your_api_key
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/
AZURE_OPENAI_EMBEDDING_DEPLOYMENT=text-embedding-3-small
AZURE_OPENAI_CHAT_DEPLOYMENT=gpt-4o-mini


### 5. Adicionar PDFs na pasta inputs/

inputs/
 ├── seu_documento.pdf


### 6. Gerar vector store

python src/vector_store.py

Saída esperada:

outputs/vector_index.faiss
outputs/metadata.pkl


### 7. Executar API

uvicorn src.api:app --reload


### 8. Acessar API

Abrir no navegador:

http://127.0.0.1:8000/docs


Interface interativa disponível via Swagger UI.

## 📡 Endpoint da API

### Base URL

http://127.0.0.1:8000


### Endpoint de consulta

POST /ask


### Descrição

Recebe uma pergunta do usuário, realiza busca semântica no vector store (FAISS) e retorna uma resposta gerada pelo Azure OpenAI com base no conteúdo dos PDFs.


### Request Body

{
  "question": "O que é uma rede LAN?"
}


### Response

{
  "answer": "Uma rede LAN (Local Area Network) é uma rede de computadores que cobre uma área geográfica limitada, como uma residência, escola ou escritório."
}


### Exemplo usando curl

curl -X POST "http://127.0.0.1:8000/ask" \
-H "Content-Type: application/json" \
-d "{\"question\": \"O que é uma rede LAN?\"}"


### Exemplo usando Python

import requests

url = "http://127.0.0.1:8000/ask"

data = {
    "question": "O que é uma rede LAN?"
}

response = requests.post(url, json=data)

print(response.json())


### Interface interativa

Disponível em:

http://127.0.0.1:8000/docs

Permite testar a API diretamente pelo navegador.

## 💬 Exemplos de Uso

### Exemplo 1 — Pergunta básica

Pergunta:

"O que é uma rede LAN?"

Resposta:

"Uma rede LAN (Local Area Network) conecta dispositivos em uma área limitada, como uma casa ou escritório."


---

### Exemplo 2 — Pergunta conceitual

Pergunta:

"Qual a diferença entre LAN e WAN?"

Resposta:

"LAN cobre uma área local, enquanto WAN cobre grandes áreas geográficas, conectando múltiplas redes LAN."


---

### Exemplo 3 — Pergunta técnica

Pergunta:

"O que é o protocolo TCP?"

Resposta:

"TCP (Transmission Control Protocol) é um protocolo de comunicação confiável que garante a entrega correta e ordenada dos dados entre dispositivos."


---

### Exemplo 4 — Uso via Python

import requests

response = requests.post(
    "http://127.0.0.1:8000/ask",
    json={"question": "O que é um roteador?"}
)

print(response.json())


---

### Exemplo 5 — Uso via curl

curl -X POST "http://127.0.0.1:8000/ask" \
-H "Content-Type: application/json" \
-d "{\"question\": \"O que é um switch de rede?\"}"


---

### Exemplo 6 — Interface Web

Abra no navegador:

http://127.0.0.1:8000/docs

Permite testar perguntas diretamente na interface Swagger.

## 🚀 Possíveis melhorias

Este projeto foi desenvolvido com arquitetura modular e permite diversas extensões para nível de produção.

### 🧠 Melhorias de IA

- Suporte a múltiplos PDFs dinâmicos via upload
- Uso de modelos mais avançados (ex: GPT-4o)
- Re-ranking semântico para melhorar precisão das respostas
- Suporte a múltiplos idiomas
- Memória de conversa (contexto persistente)


---

### ⚡ Melhorias de performance

- Uso de banco vetorial dedicado:
  - Azure AI Search
  - Pinecone
  - Weaviate
  - Qdrant

- Cache de embeddings
- Processamento assíncrono
- Paralelização da geração de embeddings


---

### 🌐 Melhorias de backend

- Autenticação com JWT
- Rate limiting
- Logs estruturados
- Monitoramento com Azure Monitor
- Tratamento avançado de erros


---

### 🖥️ Melhorias de frontend

- Interface web com React ou Next.js
- Interface estilo ChatGPT
- Upload de arquivos via interface
- Histórico de conversas


---

### ☁️ Deploy e produção

- Containerização com Docker
- Deploy no Azure App Service
- Deploy no Azure Container Apps
- CI/CD com GitHub Actions
- Deploy serverless


---

### 🧪 Melhorias de engenharia

- Testes automatizados (pytest)
- Arquitetura orientada a serviços
- Configuração via variáveis de ambiente
- Separação entre ambiente dev e produção


---

Este projeto foi idealizado com base em boas práticas modernas de engenharia de IA e pode ser facilmente evoluído para um sistema de produção completo.

<br>
<br>

# RAG Chatbot with Azure OpenAI and FAISS for Intelligent PDF Querying
The project doesn't have a specific name, so I decided to explain it.

## 📖 Project Description

This project implements an intelligent chatbot based on the Retrieval-Augmented Generation (RAG) architecture, capable of answering questions using the content of PDF documents.

The solution leverages Azure OpenAI for embeddings and contextual response generation, FAISS for high-performance vector indexing, and FastAPI to expose a professional REST API.

The system operates in four main stages:

1. PDF document ingestion
2. Text chunking into semantic segments
3. Embedding generation using Azure OpenAI
4. Vector retrieval and contextual response generation using GPT models

When a question is submitted, the system performs a semantic search across indexed documents and uses a language model to generate an accurate answer grounded in the retrieved context.

This project demonstrates practical skills in:

- Generative Artificial Intelligence
- RAG architecture
- Azure OpenAI Service
- Embeddings and vector search
- Prompt engineering
- API development with FastAPI
- PDF document processing
- Cloud service integration

This project was developed as part of the Microsoft Certification Challenge (DP-100), focusing on building real-world Machine Learning and AI solutions using Azure.

The result is a scalable, modular system ready for real-world applications such as:

- Academic assistants
- Technical support systems
- Enterprise chatbots
- Document query systems
- Scientific research assistants

## 🏗️ System Architecture

The system implements a Retrieval-Augmented Generation (RAG) pipeline using Azure OpenAI to answer questions based on PDF documents.

Execution flow:

1. Document ingestion
   - PDFs are loaded and converted to text
   - Text is split into smaller chunks

2. Embedding generation
   - Each chunk is converted into a vector using Azure OpenAI Embeddings
   - Vectors are stored in a vector database (ChromaDB)

3. User query
   - The user question is converted into an embedding
   - The system retrieves the most relevant chunks

4. Response generation
   - Retrieved chunks are sent as context to GPT-4o
   - The model generates a response grounded in the retrieved data

Simplified architecture:

User → FastAPI → Embedding → Vector Store → Context Retrieval → GPT-4o → Response

## 🧰 Tech Stack

This project was built using modern technologies for implementing Retrieval-Augmented Generation (RAG) systems.

### ☁️ Cloud & AI

- Azure OpenAI Service  
  - Generation model: GPT-4o  
  - Embedding model: text-embedding-3-large  

### 🧠 AI & Processing

- OpenAI Python SDK  
- ChromaDB (Vector Database)  
- Text chunking and embedding pipeline  

### ⚙️ Backend

- Python 3.10+
- FastAPI
- Uvicorn

### 📄 Document processing

- PyPDF
- Text ingestion and chunking pipeline

### 🔧 Supporting tools

- python-dotenv (environment variable management)
- Git and GitHub (version control)
- Python virtual environment (venv)

### 🧪 Development environment

- Visual Studio Code
- Windows 11

## 📁 Project Structure

The project structure follows software engineering best practices, separating concerns between data ingestion, AI logic, API, and vector storage.

```
chatbot-pdf-rag-azure/
│
├── inputs/                     # Source PDFs used as knowledge base
│   ├── redes_fundamentos.pdf
│   └── redes_topologias_protocolos.pdf
│
├── outputs/                    # Persisted vector store
│   ├── vector_index.faiss
│   └── metadata.pkl
│
├── src/                        # Main source code
│   ├── __init__.py             # Initializes Python module
│   ├── api.py                  # REST API using FastAPI
│   ├── chatbot.py              # Chatbot core logic (RAG)
│   ├── pdf_loader.py           # PDF loading logic
│   ├── text_chunker.py         # Text chunking logic
│   └── vector_store.py         # Vector index creation and persistence
│
├── notebooks/                  # Experiments and tests
│
├── docs/                       # Technical documentation
│
├── requirements.txt            # Project dependencies
│
├── .env                        # Environment variables (not versioned)
├── .gitignore                  # Git ignored files
└── README.md                   # Main project documentation
```
### 📌 Component Description

- src/api.py  
  Exposes the chatbot through a REST API using FastAPI.

- src/chatbot.py  
  Implements the complete RAG pipeline:
  - Receives user questions
  - Retrieves relevant documents from vector store
  - Sends context to GPT-4o
  - Returns contextualized answer

- src/create_vector_store.py  
  Responsible for:
  - Reading PDF files
  - Chunking text
  - Generating embeddings
  - Storing vectors in ChromaDB

- chroma_db/  
  Contains the persistent vector database, allowing reuse without reprocessing documents.

- data/  
  Directory containing source documents used as knowledge base.

- .env  
  Stores sensitive credentials and Azure OpenAI configuration.

## 🚀 How to run locally

### 1. Clone the repository

git clone https://github.com/YOUR-USERNAME/chatbot-pdf-rag-azure.git

cd chatbot-pdf-rag-azure


### 2. Create and activate virtual environment

Windows:

python -m venv venv
venv\Scripts\activate

Linux / Mac:

python3 -m venv venv
source venv/bin/activate


### 3. Install dependencies

pip install -r requirements.txt


### 4. Configure environment variables

Create `.env` file in project root:

AZURE_OPENAI_API_KEY=your_api_key
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/
AZURE_OPENAI_EMBEDDING_DEPLOYMENT=text-embedding-3-small
AZURE_OPENAI_CHAT_DEPLOYMENT=gpt-4o-mini


### 5. Add PDFs to inputs folder

inputs/
 ├── your_document.pdf


### 6. Generate vector store

python src/vector_store.py

Expected output:

outputs/vector_index.faiss
outputs/metadata.pkl


### 7. Run API

uvicorn src.api:app --reload


### 8. Access API

Open in browser:

http://127.0.0.1:8000/docs


Interactive interface available via Swagger UI.

## 📡 API Endpoint

### Base URL

http://127.0.0.1:8000


### Query Endpoint

POST /ask


### Description

Receives a user question, performs semantic search in the FAISS vector store, and returns an answer generated by Azure OpenAI based on PDF content.


### Request Body

{
  "question": "What is a LAN network?"
}


### Response

{
  "answer": "A LAN (Local Area Network) is a computer network that covers a limited geographic area such as a home, school, or office."
}


### Example using curl

curl -X POST "http://127.0.0.1:8000/ask" \
-H "Content-Type: application/json" \
-d "{\"question\": \"What is a LAN network?\"}"


### Example using Python

import requests

url = "http://127.0.0.1:8000/ask"

data = {
    "question": "What is a LAN network?"
}

response = requests.post(url, json=data)

print(response.json())


### Interactive interface

Available at:

http://127.0.0.1:8000/docs

Allows testing the API directly from the browser.

## 💬 Usage Examples

### Example 1 — Basic question

Question:

"What is a LAN network?"

Answer:

"A LAN (Local Area Network) connects devices within a limited area such as a home or office."


---

### Example 2 — Conceptual question

Question:

"What is the difference between LAN and WAN?"

Answer:

"LAN covers a local area, while WAN covers large geographic areas connecting multiple LANs."


---

### Example 3 — Technical question

Question:

"What is TCP protocol?"

Answer:

"TCP (Transmission Control Protocol) is a reliable communication protocol that ensures correct and ordered delivery of data between devices."


---

### Example 4 — Python usage

import requests

response = requests.post(
    "http://127.0.0.1:8000/ask",
    json={"question": "What is a router?"}
)

print(response.json())


---

### Example 5 — curl usage

curl -X POST "http://127.0.0.1:8000/ask" \
-H "Content-Type: application/json" \
-d "{\"question\": \"What is a network switch?\"}"


---

### Example 6 — Web Interface

Open in browser:

http://127.0.0.1:8000/docs

Allows testing questions directly via Swagger UI.

## 🚀 Possible Improvements

This project was built using a modular architecture and can be extended to production level.

### 🧠 AI improvements

- Support dynamic PDF upload
- Use more advanced models (ex: GPT-4o)
- Semantic re-ranking for better accuracy
- Multi-language support
- Conversation memory (persistent context)


---

### ⚡ Performance improvements

- Use dedicated vector database:
  - Azure AI Search
  - Pinecone
  - Weaviate
  - Qdrant

- Embedding cache
- Async processing
- Parallel embedding generation


---

### 🌐 Backend improvements

- JWT authentication
- Rate limiting
- Structured logging
- Azure Monitor integration
- Advanced error handling


---

### 🖥️ Frontend improvements

- Web interface using React or Next.js
- ChatGPT-style interface
- File upload support
- Conversation history


---

### ☁️ Deployment improvements

- Docker containerization
- Azure App Service deployment
- Azure Container Apps deployment
- CI/CD using GitHub Actions
- Serverless deployment


---

### 🧪 Engineering improvements

- Automated tests (pytest)
- Service-oriented architecture
- Environment-based configuration
- Dev and production environment separation


---

This project follows modern AI engineering best practices and can be evolved into a full production system.
# LangChain Fundamentals🚀

A comprehensive repository containing hands-on code examples, practice scripts, and architecture implementations exploring core concepts and workflows of the **LangChain** ecosystem.

---

## 📂 Repository Structure

The project is structured according to the fundamental components of LangChain:

```text
LangChain-Practise/
├── 🤖 AI Agent/          # Autonomous agents with tool usage and reasoning loop
├── 🔗 Chain/             # Sequential, LLM, and custom chains
├── 💬 ChatModel/         # Integrations and interactions with conversational models
├── 📄 Document Loaders/  # Ingestion of unstructured data (PDFs, Web, TXT, CSV)
├── 🧠 Embedded/          # Vector embeddings generation and vectorization strategies
├── 🔮 LLM/               # direct integrations with completion models
├── 📝 Output Parsers/    # Extracting structured outputs (JSON, Pydantic, Lists)
├── ✍️ Prompts/           # Prompt Templates, Few-Shot Prompts, and formatting
├── 📚 RAG System/        # Complete Retrieval-Augmented Generation pipelines
├── 🔎 Retriever/         # Advanced vector store retrieval techniques
├── ⚡ Runnables/          # LangChain Expression Language (LCEL) compositions
├── 🎯 StructuredOutput/  # Schema-enforced LLM responses
├── ✂️ Text Splitters/    # Document chunking strategies (Recursive, Token, Character)
├── 🛠️ Tools/             # Custom agent tools and third-party integrations
├── 🗄️ Vector Database/   # Vector store implementations (Chroma, FAISS, Pinecone, etc.)
├── .env                  # Environment variables for API credentials
├── requirements.txt      # Project dependencies
└── test.py               # Main playground script
```

---

## 🛠️ Getting Started

### 1. Prerequisites
Ensure you have Python 3.9 or higher installed on your system.

### 2. Clone the Repository
```bash
git clone https://github.com/<your-username>/LangChain-Practise.git
cd LangChain-Practise
```

### 3. Create & Activate Virtual Environment
```bash
# Create virtual environment
python -m venv venv

# Activate on Windows:
venv\Scripts\activate

# Activate on macOS/Linux:
source venv/bin/activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

### 5. Setup Environment Variables
Create a `.env` file in the root directory and add your API credentials:

```env
GEMINI_API_KEY="API_KEY_1"
GEMINI_API_KEY_2="API_KEY_2"
GEMINI_API_KEY_3="API_KEY_3"
GEMINI_API_KEY_4="API_KEY_4"
GEMINI_API_KEY_5="API_KEY_5"
HF_TOKEN="HF_TOKEN"
API_KEY="API_KEY_FOR_CURRENCY_EXCHANGE"

```

---

## 🚀 Running Examples

You can run individual scripts inside each module directory:

```bash
# Example: Testing RAG System or Prompts
python "RAG System/rag.py"
```

Or execute the global test script:

```bash
python test.py
```

---

## 📜 License

This repository is open-source and available under the [MIT License](LICENSE).
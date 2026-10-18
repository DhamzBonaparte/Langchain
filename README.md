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
OPENAI_API_KEY=your_openai_api_key
ANTHROPIC_API_KEY=your_anthropic_api_key

# Optional: LangSmith Tracing
LANGCHAIN_TRACING_V2=true
LANGCHAIN_ENDPOINT="https://api.smith.langchain.com"
LANGCHAIN_API_KEY=your_langsmith_api_key
LANGCHAIN_PROJECT="LangChain-Practise"
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
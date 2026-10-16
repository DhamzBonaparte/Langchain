from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
import os
from dotenv import load_dotenv
load_dotenv()

documents = [
    Document(page_content="LangChain helps developers build LLM applications easily."),
    Document(
        page_content="Chroma is a vector database optimized for LLM-based search."
    ),
    Document(page_content="Embeddings convert text into high-dimensional vectors."),
    Document(page_content="OpenAI provides powerful embedding models."),
]

vector_store = Chroma.from_documents(
    collection_name="my_data",
    documents=documents,
    embedding=GoogleGenerativeAIEmbeddings(
        model="gemini-embedding-001", google_api_key=os.getenv("GEMINI_API_KEY")
    ),
)

retriever = vector_store.as_retriever(search_kwargs={"k": 2})

query = "What is Chroma used for? "
res = results = retriever.invoke(query)

for i, doc in enumerate(res):
    print(f"\n--- Result {i+1} ---")
    print(doc.page_content)

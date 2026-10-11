from langchain_google_genai import GoogleGenerativeAIEmbeddings
import os
from dotenv import load_dotenv

load_dotenv()

embeddings = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-2-preview",
    dimensions=32,
    google_api_key=os.getenv("GEMINI_API_KEY_2"),
)
docs = ["I am Sulav Dhami.", "I study ML and AI.", "I have learned MERN stack."]
# vector = embeddings.embed_query("I study Machine Learning and Artificial Intelligence")
vector = embeddings.embed_documents(docs)

print(f"First 5 values: {vector[:5]}")

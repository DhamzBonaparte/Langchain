from langchain_google_genai import GoogleGenerativeAIEmbeddings
import os
from dotenv import load_dotenv

load_dotenv()

embeddings = GoogleGenerativeAIEmbeddings(model="gemini-embedding-2-preview",google_api_key=os.getenv("GEMINI_API_KEY_2"))
vector = embeddings.embed_query("I study Machine Learning and Artificial Intelligence")

print(f"First 5 values: {vector[:5]}")

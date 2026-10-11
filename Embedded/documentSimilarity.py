from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import os

load_dotenv()

embedding = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-2-preview",
    dimensions=300,
    google_api_key=os.getenv("GEMINI_API_KEY_2"),
)

docs = [
    "The morning sun cast a golden glow across the quiet valley.",
    "Deep learning architectures rely heavily on matrix multiplications and backpropagation.",
    "She opened her laptop to continue writing code for her new web project.",
    "Exploring local cafes is one of the best ways to discover a city's culture.",
    "Always verify your environment variables before running deployment scripts.",
]

query = "What does deep learning rely on?"

doc_embeddings = embedding.embed_documents(docs)
query_embedding = embedding.embed_query(query)

scores = cosine_similarity([query_embedding], doc_embeddings)[0]
index, score = sorted(list(enumerate(scores)), key=lambda x:x[1])[-1]

print(query) 
print(docs[index])
print("Similarity score : ", score)

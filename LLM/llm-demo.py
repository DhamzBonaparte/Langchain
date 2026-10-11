from dotenv import load_dotenv
import os
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-3.5-flash-lite")
result = llm.invoke("Who is the prime minister of Nepal?")
print(result.content)

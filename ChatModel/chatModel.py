from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite",
    google_api_key=os.getenv("GEMINI_API_KEY_2"),
    # temperature=0.2,  # ignored by gemini-3.5-flash-lite
    max_output_tokens=20,
)

result = model.invoke("What is the capital of Nepal?")
print(result.content[0]["text"])

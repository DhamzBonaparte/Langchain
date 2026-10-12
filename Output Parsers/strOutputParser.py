from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite", google_api_key=os.getenv("GEMINI_API_KEY_2")
)

template = PromptTemplate(
    template="Explain to me about {topic}", input_variables=["topic"]
)

template2 = PromptTemplate(
    template="Summarize about {text} in 5 points ", input_variables=["text"]
)
parser = StrOutputParser()

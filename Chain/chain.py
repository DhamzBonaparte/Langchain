from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os

load_dotenv()
prompt = PromptTemplate(
    template="Generate 5 intersting topics about {topic}", input_variables=["topic"]
)
model = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite", google_api_key=os.getenv("GEMINI_API_KEY")
)

parser = StrOutputParser()

chain = prompt | model | parser
result = chain.invoke({"topic": "Football"})
# chain.get_graph().print_ascii()
print(result)

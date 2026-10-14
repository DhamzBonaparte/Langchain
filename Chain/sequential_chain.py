from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite", google_api_key=os.getenv("GEMINI_API_KEY_2")
)

prompt = PromptTemplate(
    template="Write me in detail about topic: {topic}", input_variables=["topic"]
)

prompt2 = PromptTemplate(
    template="""
    Give me 5 points of the given information
    {details}
    such that they descrive the essence of the information
    """,
    input_variables=["details"],
)

parser = StrOutputParser()

chain = prompt | model | parser | prompt2 | model | parser

result = chain.invoke({"topic": "Mount Everest"})
print(result)

chain.get_graph().print_ascii()

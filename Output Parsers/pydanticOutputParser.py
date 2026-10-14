from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from dotenv import load_dotenv
import os

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite", google_api_key=os.getenv("GEMINI_API_KEY_2")
)

class Person(BaseModel):
    name: str = Field(description="Name of the person")
    age: int = Field(gt=18, lt=60, description="Age of the person")
    city: str = Field(description="Name of the city the person belongs to")

parser = PydanticOutputParser(pydantic_object=Person)

template = PromptTemplate(
    template="Generate the name, city and age of a fictional {place} character.\n {format_instruction}",
    input_variables=["place"],
    partial_variables={"format_instruction": parser.get_format_instructions()},
)

chain = template | model | parser
result = chain.invoke({"place": "Nepali"})

# prompt = template.invoke({"place": "Nepali"})
# result = model.invoke(prompt)
# final_res = parser.parse(result.content)
print(result)

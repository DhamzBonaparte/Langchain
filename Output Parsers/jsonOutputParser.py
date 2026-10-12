from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser
from dotenv import load_dotenv
import os

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite", google_api_key=os.getenv("GEMINI_API_KEY_2")
)

parser = JsonOutputParser()

template = PromptTemplate(
    template="Give me the name, age and city of a fictional person\n {format_instruction}",
    input_variables=[],
    partial_variables={"format_instruction": parser.get_format_instructions()},
)

chain = template | model | parser
res=chain.invoke({})
print(res)

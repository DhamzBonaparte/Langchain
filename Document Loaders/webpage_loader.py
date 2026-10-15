from langchain_community.document_loaders import WebBaseLoader
from langchain_community.document_loaders import TextLoader, WebBaseLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
import os
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite", google_api_key=os.getenv("GEMINI_API_KEY")
)

prompt = PromptTemplate(
    template="Answer the following question {ques} from the following text- \n {text}",
    input_variables=["ques", "text"],
)

parser = StrOutputParser()
loader = WebBaseLoader("https://example.com/")
docs = loader.load()

chain = prompt | model | parser

res=chain.invoke({"ques": "What is this page made for?", "text": docs[0].page_content})
print(res)

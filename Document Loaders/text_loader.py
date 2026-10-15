from langchain_community.document_loaders import TextLoader,WebBaseLoader
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
    template="Write a summary for the following poem - \n {poem}",
    input_variables=["poem"],
)

parser = StrOutputParser()
loader = TextLoader("football.txt", encoding="utf-8")
docs = loader.load()

chain = prompt | model | parser
res = chain.invoke({"poem": docs[0].page_content})
print(res)

# print(type(docs))
# print(len(docs))
# print(docs[0].page_content)
# print(docs[0].metadata)

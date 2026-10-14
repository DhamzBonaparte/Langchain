from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import (
    RunnableParallel,
    RunnableSequence,
    RunnablePassthrough,
)
from dotenv import load_dotenv
import os

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite", google_api_key=os.getenv("GEMINI_API_KEY_2")
)

prompt1 = PromptTemplate(
    template="Write a joke on topic: {topic}", input_variables=["topic"]
)
prompt2 = PromptTemplate(
    template="GIve me explaination of the joke: {joke}", input_variables=["joke"]
)

parser = StrOutputParser()

chain = RunnableSequence(prompt1, model, parser)
chain2 = RunnableSequence(prompt2, model, parser)

passed = RunnablePassthrough()

parallel_chain = RunnableParallel({"explain": chain2, "joke": passed})
final_chain = RunnableSequence(chain,parallel_chain)

res = final_chain.invoke({"topic": "AI/ML"})
print(res)

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import (
    RunnableParallel,
    RunnableSequence,
    RunnablePassthrough,
    RunnableLambda,
)
from dotenv import load_dotenv
import os

load_dotenv()


def count_words(string):
    return len(string.split())


runnable_count_words = RunnableLambda(count_words)

model = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite", google_api_key=os.getenv("GEMINI_API_KEY")
)

prompt1 = PromptTemplate(
    template="Write a joke on topic: {topic}", input_variables=["topic"]
)
prompt2 = PromptTemplate(
    template="GIve me explaination of the joke: {joke}", input_variables=["joke"]
)

parser = StrOutputParser()

chain = RunnableSequence(prompt1, model, parser)
parallel_chain = RunnableParallel(
    {"pass": RunnablePassthrough(), "lambda": runnable_count_words}
)

final_chain = RunnableSequence(chain, parallel_chain)

res = final_chain.invoke({"topic": "AI/ML"})

final_result = """{} \n word count - {}""".format(res["pass"], res["lambda"])
print(final_result)

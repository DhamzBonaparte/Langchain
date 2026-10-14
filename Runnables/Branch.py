from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import (
    RunnableParallel,
    RunnableSequence,
    RunnableBranch,
    RunnablePassthrough,
)
from dotenv import load_dotenv
import os

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite", google_api_key=os.getenv("GEMINI_API_KEY_2")
)

prompt = PromptTemplate(
    template="Write a detailed report on {topic}", input_variables=["input"]
)

prompt2 = PromptTemplate(
    template="Suummarize the follwoing text: {text}", input_variables=["text"]
)

parser = StrOutputParser()

report_gen_chain = RunnableSequence(prompt, model, parser)
branch_chain = RunnableBranch(
    (lambda x: len(x.split()) > 500, RunnableSequence(prompt2, model, parser)),
    RunnablePassthrough(),
)

final_chain = RunnableSequence(report_gen_chain, branch_chain)

res = final_chain.invoke({"topic": "Nepal being a landlocked country"})
print(res)

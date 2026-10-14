from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.runnables import RunnableBranch, RunnableLambda, RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal
from dotenv import load_dotenv
import os

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite", google_api_key=os.getenv("GEMINI_API_KEY_5")
)

parser = StrOutputParser()

class Sentiment(BaseModel):
    sentiment: Literal["posetive", "negative"] = Field(
        description="Give the sentiment of the feedback"
    )

pydantic_parser = PydanticOutputParser(pydantic_object=Sentiment)

prompt = PromptTemplate(
    template="Classify the sentiment of the following feedback text into posetive or negative \n {feedback} \n {format_instruction}",
    input_variables=["feedback"],
    partial_variables={"format_instruction": pydantic_parser.get_format_instructions()},
)

classifier_chain = RunnablePassthrough.assign(
    sentiment=prompt | model | pydantic_parser
)

neg_prompt = PromptTemplate(
    template="Write an appropriate feedback for this negative feedback to give to the reviewer. \n {feedback}",
    input_variables=["feedback"],
)

pos_prompt = PromptTemplate(
    template="Write an appropriate feedback for this posetive feedback to give to the reviewer. \n {feedback}",
    input_variables=["feedback"],
)

branch_chain = RunnableBranch(
    (lambda x: x["sentiment"].sentiment == "posetive", pos_prompt | model | parser),
    (lambda x: x["sentiment"].sentiment == "negative", neg_prompt | model | parser),
    RunnableLambda(lambda x: x["sentiment"].sentiment),
)

chain = classifier_chain | branch_chain

result = chain.invoke({"feedback": "This is a bad phone"})
print(result)

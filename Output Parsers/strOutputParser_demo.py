from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()

llm = HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0", task="text-generation"
)

model = ChatHuggingFace(llm=llm)

template1 = PromptTemplate(
    template="Write a detailed report on {topic}", input_variables=["topic"]
)

template2 = PromptTemplate(
    template="Write a 5 line summary on the given following text. /n {topic}",
    input_variables=["topic"],
)

prompt1 = template1.invoke({"topic": "black hole"})
result1 = model.invoke(prompt1)

prompt2 = template1.invoke({"topic": result1["content"]})
result2 = model.invoke(prompt2)

print(result2.content)

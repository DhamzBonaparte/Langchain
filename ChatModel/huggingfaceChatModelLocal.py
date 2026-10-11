from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
import os

llm = HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    pipeline_kwargs={"max_new_tokens": 20, "temperature": 0.5},
)
model = ChatHuggingFace(llm=llm)
result = model.invoke("What is the capital of Nepal?")
print(result.content)

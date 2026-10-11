from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
from dotenv import load_dotenv

import os

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite", google_api_key=os.getenv("GEMINI_API_KEY_5")
)

chat_history = [
    SystemMessage(content="You are a helpful AI Assistant.")
]

while True:
    user_input = input("You: ")
    chat_history.append(HumanMessage(user_input))
    if user_input == "exit":
        break
    result = model.invoke(chat_history)
    chat_history.append(AIMessage(result.content[0]["text"]))
    print("AI: ", result.content[0]["text"])

print(chat_history)
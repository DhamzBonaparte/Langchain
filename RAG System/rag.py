from youtube_transcript_api import (
    YouTubeTranscriptApi,
    TranscriptsDisabled,
    FetchedTranscriptSnippet,
)
from langchain_classic.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from transcript import transcript
import os
from langchain_core.documents import Document
from dotenv import load_dotenv
from langchain_core.runnables import (
    RunnableLambda,
    RunnableSequence,
    RunnableParallel,
    RunnablePassthrough,
)

load_dotenv()

transcript_str = " "
for snippet in transcript:
    transcript_str += "".join(snippet.text)

splitter = RecursiveCharacterTextSplitter(chunk_size=150, chunk_overlap=20)
chunks = splitter.split_text(transcript_str)

embedding = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-2-preview",
    google_api_key=os.getenv("GEMINI_API_KEY_4"),
)

vector_store = FAISS.from_texts(texts=chunks, embedding=embedding)

retreiver = vector_store.as_retriever(search_type="similarity", search_kwargs={"k": 4})

llm = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite", google_api_key=os.getenv("GEMINI_API_KEY_5")
)

prompt = PromptTemplate(
    template="""
                        You are a helpful Assistant.
                        Answer ONLY from the provided transcript context.
                        If the context is insufficient, just say I dont know.
                        
                        {context}
                        question: {question}
                        """,
    input_variables=["context", "question"],
)

parser = StrOutputParser()

def format_docs(retrieved_docs):
    context_Text = "\n\n".join(doc.page_content for doc in retrieved_docs)
    return context_Text

parallel_chain = RunnableParallel(
    {
        "context": retreiver | RunnableLambda(format_docs),
        "question": RunnablePassthrough(),
    }
)

main_chain = parallel_chain | prompt | llm | parser
res=main_chain.invoke("Can you summarize the video?")
print(res)

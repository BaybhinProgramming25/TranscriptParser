import os 
import chromadb

from dotenv import load_dotenv
from langchain_anthropic import ChatAnthropic
from langchain_chroma import Chroma 
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_huggingface import HuggingFaceEmbeddings
from fastapi import APIRouter 

load_dotenv()
router = APIRouter()
chroma_client = chromadb.PersistentClient(path="../PersistentData/chroma_db")


@router.post('/qa')
def answer_question(data: dict):

    question = data["question"]

    api_key = os.getenv("ANTHROPIC_API_KEY")
    os.environ["ANTHROPIC_API_KEY"] = api_key

    llm = ChatAnthropic(model="claude-sonnet-4-5-20250929", temperature=0.7)
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

    vector_store = Chroma(
        client=chroma_client,
        collection_name='student-data',
        embedding_function=embeddings
    )

    retriever = vector_store.as_retriever()

    prompt = ChatPromptTemplate.from_template("""
    # Answer based on this context: {context}
                                              
    # Question: {question}
    """)

    chain = (
        {"context": retriever, "question": RunnablePassthrough()}
        | prompt
        | llm 
    )

    response = chain.invoke(question)
    print(response)
from fastapi import APIRouter, UploadFile, File, Form 
from typing import Optional
from middleware.parser.query import parse_pdf

from langchain_chroma import Chroma 
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_ollama import OllamaLLM
from langchain_community.embeddings import OllamaEmbeddings
from langchain_core.output_parsers import StrOutputParser

router = APIRouter()

@router.post('/parse')
async def parse(
    file: Optional[UploadFile] = File(None),
    message: str = Form(...)
):
    response = {
        "message": message,
        "has_file": False 
    }

    pdf_content = ""
    if file:
        file_bytes = await file.read()
        pdf_content = parse_pdf(file_bytes)
        response["has_file"] = True 


    llm = OllamaLLM(model="phi3", base_url='http://ollama:11434')
    embeddings = OllamaEmbeddings(model="nomic-embed-text", base_url='http://ollama:11434')

    vectorstore = Chroma(
        collection_name='cs-grad-requirements',
        embedding_function=embeddings,
        host="chromadb",
        port=8000
    )

    retriever = vectorstore.as_retriever()

    prompt = ChatPromptTemplate.from_template("""

            You are a helpful assistant that will answer questions based on the provided document content. 
            Keep in mind that sometimes there will be NO provided document content, so you will have to rely solely on the database
                                              
            DATABASE CONTEXT:
            {context}
                                              
            DOCUMENT CONTENT:
            {pdf_content}

            QUESTION:
            {question}             

            ANSWER:                                 
    """)

    chain = (
        {"context": retriever, "pdf_content": lambda _: pdf_content,  "question": RunnablePassthrough() }
        | prompt
        | llm
        | StrOutputParser()
    )

    # Invoke
    response = chain.invoke(message)
    print(response)

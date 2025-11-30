from fastapi import APIRouter, UploadFile, File, Form
from typing import Optional, List
from middleware.parser.query import parse_pdf

from langchain_chroma import Chroma 
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_ollama import OllamaLLM, OllamaEmbeddings
from langchain_core.output_parsers import StrOutputParser

router = APIRouter()


# Alot more work to do here 
@router.post('/parse')
async def parse(
    file: Optional[UploadFile] = Form(None),
    message: str = Form(...)
):
    response = {
        "message": message,
        "has_file": False 
    }

    # If file present, we then parse and store in ChromaDB 
    if file:
        file_bytes = await file.read()
        parse_pdf(file_bytes)
        response["has_file"] = True 
   
    llm = OllamaLLM(model="phi3", base_url='http://ollama:11434')
    embeddings = OllamaEmbeddings(model="nomic-embed-text", base_url='http://ollama:11434')

    vectorstore = Chroma(
        collection_name='student-transcript-data',
        embedding_function=embeddings,
        
    )
    retriever = vectorstore.as_retriever(
        search_kwargs={"k": 10}
    )


    prompt = ChatPromptTemplate.from_template("""
                                              
            Here is information provided in the database:
                                              
            {context}
                                              
            Question: {question}
                                              
            IMPORTANT RULES:
            - Only use the information that is explicitly stated in the database
            - If the information is not in the database, say "I can't make a proper conclusion cause the information is not provided in the database"
            - Absolutely do not make assumptions or infer information that isn't directly stated
            - Quote specific parts of the database when answering
            - If you are unsure, say so 
                                              
            Please answer based ONLY on the database information provided.                             
    """)

    chain = (
        {"context": retriever,  "question": RunnablePassthrough() }
        | prompt
        | llm
        | StrOutputParser()
    )

    test_docs = retriever.invoke(message)
    print(f"\n=== RETRIEVED {len(test_docs)} DOCUMENTS ===")
    for i, doc in enumerate(test_docs):
        print(f"\n--- Document {i+1} ---")
        print(doc.page_content[:200])  # First 200 chars
    print("=" * 50 + "\n")

    # Invoke
    response = chain.invoke(message)
    print(response)

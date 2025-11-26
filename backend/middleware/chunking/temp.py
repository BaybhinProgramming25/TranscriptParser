from langchain_ollama import OllamaLLM
from langchain_community.vectorstores import Chroma
from langchain_ollama import OllamaEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough()

# Set up ollama 
def ollama_configure():

    llm = OllamaLLM(model="llama3:8b")
    embeddings = OllamaEmbeddings(model="llama3:8b")

    # Connect to chromaDB
    vectorstore = Chroma(
        collection_name=("cs-grad-requirements"),
        embedding_function=embeddings,
        persist_directory="../chroma-data/"
    )
    retriever = vectorstore.as_retriever()

    # Construct the ChatPrompt
    prompt = ChatPromptTemplate.from_template("""
    # Answer based on this context: {context}
                                              
    # Question: {question}
    """)

    # Make the chain 
    chain = (
        {"context": retriever, "question": RunnablePassthrough() 
        | prompt 
        | llm}
    )

    # Answer the question
    response = chain.invoke(question)
    print(response )
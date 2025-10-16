import chromadb

from fastapi import APIRouter 

router = APIRouter()
chroma_client = chromadb.PersistentClient(path="../PersistentData/chroma_db")

try:
    collection = chroma_client.get_collection(name='student-data')
except:
    collection = chroma_client.create_collection(name='student-data')


# Move these routes in their own separate files later 
@router.post("/setup-db")
def setup(semester_data: dict):

    ids, documents = [], []
    for key, value in semester_data.items():
        ids.append(key)
        documents.append(value)

    # Add some text documents to the collection 
    collection.add(
        ids=ids,
        documents=documents
    )
    


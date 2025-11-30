from pymongo import AsyncMongoClient

client = None 
db = None 
users_collection = None
contacts_collection = None 

async def connect_mongo():

    global client, db, users_collection, contacts_collection
    client = AsyncMongoClient("mongodb://mongodb:27017")
    db = client.get_database("usersTQA")
    users_collection = db.get_collection("users")
    contacts_collection = db.get_collection("contacts")
    print("Connected to MongoDB!", flush=True)

async def close_mongo():
    
    global client 
    if client:
        client.close()
        print("Closed MongoDB")


def get_users_collection():
    if client:
        return users_collection

def get_contacts_collection():
    if client:
        return contacts_collection
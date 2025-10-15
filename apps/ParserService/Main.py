import requests
from fastapi import FastAPI

app = FastAPI()

from Controllers.Parse import router as parse_router 

app.include_router(parse_router)

if __name__ == "__main__":
    import uvicorn 
    uvicorn.run(app, host="127.0.0.1", port=8000)
    
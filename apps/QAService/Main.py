from fastapi import FastAPI

app = FastAPI()

from Controllers.AnswerQuestion import router as qa_router 

app.include_router(qa_router)

if __name__ == "__main__":
    import uvicorn 
    uvicorn.run(app, host='127.0.0.1', port=8002)
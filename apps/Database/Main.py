from fastapi import FastAPI

app = FastAPI()

from Controllers.Setup import router as setup_router

app.include_router(setup_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=8001)
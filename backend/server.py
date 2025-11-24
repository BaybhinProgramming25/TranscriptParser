from fastapi import FastAPI
from controllers.qa import router as true_router 

app = FastAPI()
app.include_router(true_router)


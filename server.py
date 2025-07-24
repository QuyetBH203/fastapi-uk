from fastapi import FastAPI
from core.config import config
from core.db import session

app = FastAPI()




@app.get("/",tags=["healthcheck"])
async def root():
    print(session)
  
    return {"message": "Hello World"}
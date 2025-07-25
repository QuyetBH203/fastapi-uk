from fastapi import FastAPI
from enum import Enum
from fastapi.middleware.cors import CORSMiddleware
from core.di import init_di

# Initialize dependency injection before importing controllers
init_di()

# Import controllers after DI initialization
from app.controller import module_router

app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.get("/",tags=["healthcheck"])
async def root():
    return {"message": "Hello World"}


app.include_router(module_router)
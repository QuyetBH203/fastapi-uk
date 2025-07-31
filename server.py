from fastapi import FastAPI
from enum import Enum
from fastapi.middleware.cors import CORSMiddleware
from core.middlewares import SQLAlchemyMiddleware
from core.di import init_di
from core.config import config


init_di()
from app.controller import module_router

app = FastAPI(
    title="FastAPI UK",
    description="A FastAPI project template for UK developers",
    version="0.1.0",
    docs_url=None if config.ENV == "production" else "/docs",
    redoc_url=None if config.ENV == "production" else "/redoc",
)

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
app.add_middleware(SQLAlchemyMiddleware)


@app.get("/",tags=["healthcheck"])
async def root():
    return {"message": "Hello World"}


app.include_router(module_router)
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from core.config import config
from app.controller import employee_router

app = FastAPI(
    title="Employee Management System",
    description="Employee Management System API",
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


@app.get("/",tags=["healthcheck"])
async def root():
    return {"message": "Hello World"}


app.include_router(employee_router)
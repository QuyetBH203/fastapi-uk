from fastapi import FastAPI


app = FastAPI()


# @app.on_event("startup")
# async def startup_event():
   
#     try:
#         test_connection()
#         print("Database connection successful")
#     except Exception as e:
#         print(f"Database connection failed: {e}")


@app.get("/",tags=["healthcheck"])
async def root():
    return {"message": "Hello World"}
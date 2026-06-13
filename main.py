from fastapi import FastAPI
from scalar_fastapi import get_scalar_api_reference
from pydantic import BaseModel
from dotenv import load_dotenv

from app.router import router

load_dotenv()
app = FastAPI()

@app.get("/")
def say_hello():
    return {"message": "Hai"}

app.include_router(router)

@app.get("/scalar")
def get_scalar():    
    return get_scalar_api_reference(
        title=app.title,
        openapi_url=app.openapi_url
    )
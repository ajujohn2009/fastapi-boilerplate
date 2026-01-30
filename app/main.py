from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI(title="Hello World")

@app.get("/")
def main():
    return {"message": "Hello World latest code version2 1"}


@app.get("/health")
def health_check():
    return {"status": "OK"}

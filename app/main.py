from fastapi import FastAPI
from app.core.config import settings

app = FastAPI(title=settings.project_name)

@app.get("/")
def root():
    return {
        "mesage" : "Hello from Task Tracker",
        "debug": settings.debug
    }
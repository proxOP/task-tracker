from fastapi import FastAPI
from app.core.config import settings
from app.api import tasks, users

app = FastAPI(title=settings.project_name)

app.include_router(users.router)
app.include_router(tasks.router)

@app.get("/")
def health_check():
    return ({"status": "ok", "message": "Task Tracker API is running!"})
    
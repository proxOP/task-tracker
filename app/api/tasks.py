from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.schemas.task import TaskCreate, TaskRead
from app.services import crud

router = APIRouter(prefix="/tasks", tags=["tasks"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=TaskRead, status_code=201)
def create_task(task_in: TaskCreate, db: Session = Depends(get_db)):
    return crud.create_task(db, task_in)

@router.get("/", response_model=list[TaskRead])
def list_tasks(assignee_id: int | None = Query(None), db: Session = Depends(get_db)):
    tasks = crud.list_tasks(db, assignee_id)
    return tasks        
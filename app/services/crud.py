from sqlalchemy.orm import Session
from app.models import User, Task
from app.schemas.user import UserCreate
from app.schemas.task import TaskCreate

# ------------------USERS------------------
def create_user(db: Session, user_in: UserCreate) -> User:
    user = User(**user_in.dict())
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def get_user(db: Session, user_id: int) -> User | None:
    return db.get(User, user_id)


# ------------------TASKS------------------
def create_task(db: Session, task_in: TaskCreate) -> Task:
    task = Task(**task_in.dict())
    db.add(task)
    db.commit()
    db.refresh(task)
    return task

def list_tasks(db: Session, assignee_id: int | None = None) -> list[Task]:
    q = db.query(Task)
    if assignee_id is not None:
        q = q.filter(Task.assignee_id == assignee_id)
    return q.all()
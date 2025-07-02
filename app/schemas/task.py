from pydantic import BaseModel, ConfigDict

class TaskBase(BaseModel):
    title: str
    describtion : str | None = None

class TaskCreate(TaskBase):
    assignee_id: int

class TaskRead(TaskBase):
    id: int
    assignee_id: int

    model_config = ConfigDict(from_attributes=True)   
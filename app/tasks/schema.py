from pydantic import BaseModel, Field


class TaskBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=100, description="Task title")
    description: str = Field(None, min_length=1, max_length=500, description="Task description")
    is_completed: bool = Field(..., description="Task completion status")



class TaskCreate(TaskBase):
    pass

class TaskUpdate(TaskBase):
    pass

class TaskResponse(TaskBase):
    id: int = Field(..., description="Task ID")
    created_at: str = Field(..., description="Task creation timestamp")
    updated_at: str = Field(..., description="Task update timestamp")


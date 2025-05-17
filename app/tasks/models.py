from sqlalchemy import Column, Integer, String, Text,Boolean, func 

from core.config.database import Base

class TaskModel(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String(255), nullable=False)
    description = Column(Text(500), nullable=True)
    is_completed = Column(Boolean, default=False)
    created_at = Column(String(50), server_default=func.now())
    updated_at = Column(String(50), server_default=func.now(), onupdate=func.now())

    def __repr__(self):
        return f"<Task {self.id}>"
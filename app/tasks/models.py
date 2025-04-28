from sqlalchemy import Column, Integer, String,func 

from core.config.database import Base

class TaskModel(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    description = Column(String(255), nullable=False)
    created_at = Column(String(50), default=func.now())
    updated_at = Column(String(50), default=func.now(), onupdate=func.now())

    def __repr__(self):
        return f"<Task {self.id}>"
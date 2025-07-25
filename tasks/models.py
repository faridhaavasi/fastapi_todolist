from core.database import Base
from sqlalchemy import Boolean, Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(Text, default="")
    is_done = Column(Boolean, default=False)

    user_id = Column(Integer, ForeignKey("users.id")) 
    user = relationship("UserModel", back_populates="tasks")  

    def __repr__(self) -> str:
        return f"Task(id={self.id!r}, title={self.title!r}, is_done={self.is_done!r})"

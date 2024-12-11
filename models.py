# models.py
from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.ext.declarative import declarative_base
import enum

Base = declarative_base()

class TaskStatus(enum.Enum):
    PENDING = "Pendiente"
    COMPLETED = "Completada"

class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    status = Column(Enum(TaskStatus), default=TaskStatus.PENDING)

    def __repr__(self):
        return f"<Task(id={self.id}, title={self.title}, status={self.status})>"

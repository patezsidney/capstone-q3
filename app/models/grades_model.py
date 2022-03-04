from dataclasses import dataclass
from sqlalchemy import Column, String, Float, Integer
from uuid import uuid4
from sqlalchemy.dialects.postgresql import UUID
from app.configs.database import db

@dataclass
class GradesModel(db.Model):
    __tablename__ = "grades"

    grade_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    ativity:str = Column(String, nullable=False)
    grade:float = Column(Float, nullable=False)
    # student_id = Column(Integer, ForeignKey("student.id"), nullable=False)
    # classrom_id:str = Column(Integer, ForeignKey("classrom.id"), nullable=False)

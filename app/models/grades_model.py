from dataclasses import dataclass
from sqlalchemy import Column, String, Float, ForeignKey
from uuid import uuid4
from sqlalchemy.dialects.postgresql import UUID
from app.configs.database import db

@dataclass
class GradesModel(db.Model):
    __tablename__ = "grades"

    grade_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    ativity:str = Column(String, nullable=False)
    grade:float = Column(Float, nullable=False)
    student_id: str = Column(String, ForeignKey("students.registration_student_id"),nullable=False)
    classrom_id:str = Column(String, ForeignKey("classrom.classroom_id"), nullable=False)

from dataclasses import dataclass
from uuid import uuid4

from sqlalchemy import Column, Float, ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID

from app.configs.database import db


@dataclass
class GradesModel(db.Model):
    __tablename__ = "grades"

    grade_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    ativity:str = Column(String, nullable=False)
    grade:float = Column(Float, nullable=False)
    student_id: str = Column(UUID, ForeignKey("students.registration_student_id"),nullable=False)
    classrom_id:str = Column(UUID, ForeignKey("classrooms.classroom_id"), nullable=False)

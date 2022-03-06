from dataclasses import dataclass
from sqlalchemy import Column, Date, Boolean, ForeignKey
from uuid import uuid4
from sqlalchemy.dialects.postgresql import UUID
from app.configs.database import db

@dataclass
class AbsenceModel(db.Model):
    __tablename__ = "absence"

    absence_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    date:str = Column(Date)
    justify:bool = Column(Boolean, default=False)
    classroom_id:str = Column(UUID, ForeignKey("classrooms.classroom_id"), nullable=False)
    student_id = Column(UUID, ForeignKey("students.registration_student_id"), nullable=False)

from dataclasses import dataclass
from uuid import uuid4

from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID

from app.configs.database import db


@dataclass
class SchoolSubjectsModel(db.Model):
    __tablename__ = "schoolsubjects"
    school_subject_id:str = Column(UUID(as_uuid=True),primary_key=True,default=uuid4)
    school_subject:str = Column(String(255),nullable=False)
    employee_id: str = Column(UUID,ForeignKey("employees.employee_id"),nullable=False)
    classroom_id: str = Column(UUID,ForeignKey("classrooms.classroom_id"),nullable=False)

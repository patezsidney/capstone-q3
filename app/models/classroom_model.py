from dataclasses import dataclass
from uuid import uuid4

from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship, backref

from app.configs.database import db


@dataclass
class ClassroomModel(db.Model):
    __tablename__="classrooms"
    classroom_id:str = Column(UUID(as_uuid=True),primary_key=True, default=uuid4)
    name:str = Column(String(255),nullable=False)
    school_subjects = relationship("SchoolSubjectsModel",backref="classroom")
    absences = relationship("AbsenceModel",backref="classroom")
    grades = relationship("GradesModel",backref=backref("classroom"))
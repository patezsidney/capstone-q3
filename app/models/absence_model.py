from dataclasses import dataclass
from uuid import uuid4

from sqlalchemy import Boolean, Column, Date, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import validates

from app.configs.database import db
from app.models.exc import IncorrectKeyError


@dataclass
class AbsenceModel(db.Model):

    absence_id: str
    date: str
    justify: bool
    classroom_id: str
    student_id: str

    __tablename__ = "absence"

    absence_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    date:str = Column(Date)
    justify:bool = Column(Boolean, default=False)
    classroom_id:str = Column(UUID, ForeignKey("classrooms.classroom_id"), nullable=False)
    student_id = Column(UUID, ForeignKey("students.registration_student_id"), nullable=False)


    @validates('date',  'classroom_id', 'student_id')
    def validate_type(self, key, value):
        if type(value) != str:
            raise IncorrectKeyError
        return value
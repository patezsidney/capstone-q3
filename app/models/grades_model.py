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

    @staticmethod
    def serialize(data):
        output = []
        if type(data) == list:
            for one in data:
                output.append({
                    "ativity": one.ativity,
                    "grade": one.grade,
                    "student": {"student_id" : one.student.registration_student_id, "name": one.student.name},
                    "classrom": one.classroom
                    })
        else:
            output = {
                    "ativity": data.ativity,
                    "grade": data.grade,
                    "student": {"student_id" : data.student.registration_student_id, "name": data.student.name},
                    "classrom": data.classroom
                    }


        return output

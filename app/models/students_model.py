from dataclasses import dataclass
from uuid import uuid4

from sqlalchemy import Column, Date, ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import backref, relationship
from werkzeug.security import check_password_hash, generate_password_hash

from app.configs.database import db
from app.models.absence_model import AbsenceModel
from app.models.exc import IncorrectKeyError, MissingKeyError,TypeValueError


@dataclass
class StudentsModel(db.Model):
    registration_student_id: str
    name: str
    contact_name: str
    contact_email: str
    cpf: str
    birth_date: str
    absences: AbsenceModel

    __tablename__ = 'students'

    registration_student_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    name = Column(String(255), nullable=False)
    contact_name = Column(String(255), nullable=False)
    contact_email = Column(String(255), nullable=False)
    cpf = Column(String(11), nullable=False, unique=True)
    birth_date = Column(Date, nullable=False)
    gender = Column(String(50))
    photo = Column(String)
    password_hash = Column(String)
    classroom_id = Column(UUID,ForeignKey("classrooms.classroom_id"),nullable=False)
    api_key = Column(String)
    grades = relationship("GradesModel",backref=backref("stundent",uselist=False))
    absences = relationship("AbsenceModel",backref=backref("student",uselist=False))
    classroom = relationship("ClassroomModel",backref="students",uselist=False)

    @property
    def password(self):
        raise AttributeError("Password is not accessible")

    @password.setter
    def password(self, password_to_hash):
        self.password_hash = generate_password_hash(password_to_hash)

    def check_password(self, password_to_compare):
        return check_password_hash(self.password_hash, password_to_compare)

    @classmethod
    def check_incorrect_keys(cls,data):
        if len([key for key in data.keys() if key not in ["name","contact_name","contact_email","cpf","birth_date","gender","photo","password","classroom_id"]]):
            raise IncorrectKeyError        
        return True

    @classmethod
    def check_keys(cls,data):
        if len([key for key in ["name","contact_name","contact_email","cpf","birth_date","gender","photo","password","classroom_id"] if key not in data.keys()]):
            raise MissingKeyError        
        return True

    @classmethod
    def check_type_value(cls,data):
        if len([value for value in data.values() if type(value)!= str]):
            raise TypeValueError
        return True

    @staticmethod
    def serialize(data):
        output = []
        if type(data) == list:
            for student in data:
                output.append({
                    "id":student.registration_student_id,
                    "name":student.name,
                    "cpf": student.cpf,
                    "birth_date": student.birth_date,
                    "contact_name":student.contact_name,
                    "contact_email":student.contact_email,
                    "gender": student.gender
                    })
        else:
            output = {
                    "id":data.registration_student_id,
                    "name":data.name,
                    "cpf": data.cpf,
                    "birth_date": data.birth_date,
                    "contact_name":data.contact_name,
                    "contact_email":data.contact_email,
                    "gender": data.gender

                }

        return output

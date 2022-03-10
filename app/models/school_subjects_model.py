from dataclasses import dataclass
from uuid import uuid4

from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID

from app.configs.database import db
from app.models.exc import IncorrectKeyError, MissingKeyError, TypeValueError


@dataclass
class SchoolSubjectsModel(db.Model):
    __tablename__ = "schoolsubjects"
    school_subject_id:str = Column(UUID(as_uuid=True),primary_key=True,default=uuid4)
    school_subject:str = Column(String(255),nullable=False)
    employee_id: str = Column(UUID,ForeignKey("employees.employee_id"),nullable=False)
    classroom_id: str = Column(UUID,ForeignKey("classrooms.classroom_id"),nullable=False)

    @classmethod
    def check_incorrect_keys(cls,data):
        if len([key for key in data.keys() if key not in ["school_subject","employee_id","classroom_id"]]):
            raise IncorrectKeyError        
        return True

    @classmethod
    def check_keys(cls,data):
        if len([key for key in ["school_subject","employee_id","classroom_id"] if key not in data.keys()]):
            raise MissingKeyError        
        return True
    
    @classmethod
    def check_type_value(cls,data):
        if len([value for value in data.values() if type(value)!= str]):
            raise TypeValueError
        return True

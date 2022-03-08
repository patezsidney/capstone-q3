from dataclasses import dataclass
from datetime import datetime, timedelta
from uuid import uuid4

from sqlalchemy import Column, Date, ForeignKey
from sqlalchemy.dialects.postgresql import UUID

from app.configs.database import db
from app.models.exc import IncorrectKeyError, MissingKeyError, TypeValueError


@dataclass
class LibraryModel(db.Model):

    __tablename__ = "library"

    library_id: str = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    date_withdrawal: str = Column(Date, nullable=False, default=datetime.now())
    date_return: str = Column(Date, nullable=True)
    date_accurancy: str = Column(Date, nullable=False, default=(datetime.now() + timedelta(15)))
    employee_id:str = Column(UUID,ForeignKey("employees.employee_id"),nullable=False)
    book_id:str = Column(UUID,ForeignKey("books.book_id"),nullable=False)
    student_id:str = Column(UUID,ForeignKey("students.registration_student_id"),nullable=False)

    @classmethod
    def check_incorrect_keys(cls,data):
        if len([key for key in data.keys() if key not in ["employee_id","book_id","student_id"]]):
            raise IncorrectKeyError        
        return True

    @classmethod
    def missing_key(cls,data):
        if len([key for key in ["employee_id","book_id","student_id"] if key not in data.keys()]):
            raise MissingKeyError        
        return True

    @classmethod
    def check_key_in_edit_book_or_student_in_rental(cls,data):
        if len([key for key in data.keys() if key not in ["book_id","student_id"]]):
            raise IncorrectKeyError        
        return True

    @classmethod
    def check_type_value(cls,data):
        if len([value for value in data.values() if type(value)!=str]):
            raise TypeValueError
        return True


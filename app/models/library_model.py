from dataclasses import dataclass
from datetime import datetime, timedelta
from uuid import uuid4

from sqlalchemy import Column, Date, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from app.models.exc import IncorrectKeyError,MissingKeyError

from app.configs.database import db


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
        key_error = [key for key in data.keys() if key not in ["employee_id","book_id","student_id"]]

        if len(key_error) > 0:
            raise IncorrectKeyError
        
        return True

    @classmethod
    def missing_key(cls,data):
        key_error = [key for key in ["employee_id","book_id","student_id"] if key not in data.keys()]

        if len(key_error) > 0:
            raise MissingKeyError
        
        return True


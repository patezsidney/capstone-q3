from dataclasses import dataclass
from datetime import datetime, timedelta
from uuid import uuid4

from sqlalchemy import Column, Date, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship,backref

from app.configs.database import db


@dataclass
class LibraryModel(db.Model):

    library_id: str
    date_withdrawal: str
    date_accurancy: str
    book_id: str
    student_id: str
    employee_id: str

    __tablename__ = "library"

    library_id: str = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    date_withdrawal: str = Column(Date, nullable=False, default=datetime.now())
    date_return: str = Column(Date, nullable=True)
    date_accurancy: str = Column(Date, nullable=False, default=(datetime.now() + timedelta(15)))
    employee_id:str = Column(UUID,ForeignKey("employees.employee_id"),nullable=False)
    book_id:str = Column(UUID,ForeignKey("books.book_id"),nullable=False)
    student_id:str = Column(UUID,ForeignKey("students.registration_student_id"),nullable=False)

    employee = relationship("EmployeeModel", backref=backref("employee"))
    student = relationship("StudentsModel", backref=backref("student"))
    book = relationship("BooksModel", backref=backref("book"))
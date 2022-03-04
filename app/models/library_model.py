from dataclasses import dataclass
from datetime import datetime, timedelta
from sqlalchemy import Column, Date, ForeignKey
from app.configs.database import db

from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4

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

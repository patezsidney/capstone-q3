from uuid import uuid4
from werkzeug.security import generate_password_hash, check_password_hash

from sqlalchemy import Column, String, Date
from sqlalchemy.dialects.postgresql import UUID

from app.configs.database import db


class StudentsModel(db.Model):

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
    api_key = Column(String)

    @property
    def password(self):
        raise AttributeError("Password is not accessible")

    @password.setter
    def password(self, password_to_hash):
        self.password_hash = generate_password_hash(password_to_hash)

    def check_password(self, password_to_compare):
        return check_password_hash(self.password_hash, password_to_compare)
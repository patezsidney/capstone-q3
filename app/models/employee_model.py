from uuid import uuid4
from werkzeug.security import generate_password_hash, check_password_hash
from dataclasses import dataclass
from sqlalchemy import Column, VARCHAR, Float
from sqlalchemy.orm import validates
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship, backref
import re


from app.configs.database import db
from app.models import school_subjects_model
from app.models.exc import EmailError, EmployeeAtributeTypeError

@dataclass
class EmployeeModel(db.Model):
    
    employee_id: str
    name: str
    email: str
    wage: float
    access_level: str

    __tablename__ = 'employees'

    employee_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    name = Column(VARCHAR(255), nullable=False)
    email = Column(VARCHAR(255), nullable=False, unique=True)
    wage = Column(Float)
    password_hash = Column(VARCHAR)
    api_key = Column(VARCHAR)
    access_level = Column(VARCHAR, nullable=False)
    library = relationship("LibraryModel",backref=backref("librarian",uselist=False))
    school_subjects = relationship("SchoolSubjectsModel",backref="employees")

    @property
    def password(self):
        raise AttributeError('Não é possivel acessar a senha dos usuários')
    
    @password.setter
    def password(self, password_to_hash):
        self.password_hash = generate_password_hash(password_to_hash)
    
    def check_password(self, passsword_to_compare):
        return check_password_hash(self.password_hash, passsword_to_compare)

    @validates('email')
    def validate_email(self, key, value):
        if not re.match(r"^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$", value):
            raise EmailError()
        
        if type(value) != str:
            raise EmployeeAtributeTypeError()
        return value

    @validates('employee_id',  'name', 'wage', 'access_level')
    def validate_type(self, key, value):
        if key == 'wage':
            if type(value) != float:
                raise EmployeeAtributeTypeError()
        else:
            if type(value) != str:
                raise EmployeeAtributeTypeError()
        return value


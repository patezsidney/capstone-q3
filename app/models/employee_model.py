import re

from dataclasses import dataclass
from sqlalchemy import Column, VARCHAR, Float
from sqlalchemy.orm import validates

from app.configs.database import db
from app.models.exc import EmailError, EmployeeAtributeTypeError

@dataclass
class EmployeeModel(db.Model):
    
    employee_id: str
    name: str
    email: str
    wage: float
    access_level: str

    __tablename__ = 'employees'

    employee_id = Column(VARCHAR, primary_key=True)
    name = Column(VARCHAR(255), nullable=False)
    email = Column(VARCHAR(255), nullable=False, unique=True)
    wage = Column(Float)
    password_hash = Column(VARCHAR)
    api_key = Column(VARCHAR)
    access_level = Column(VARCHAR, nullable=False)

    @property
    def password(self):
        raise AttributeError('Não é possivel acessar a senha dos usuários')
    
    @password.setter
    def password(self, password_to_hash):
        ...
    
    def check_password(self, passsword_to_compare):
        ...

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


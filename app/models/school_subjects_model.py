from app.configs.database import db
from sqlalchemy import Column,String,Integer
from dataclasses import dataclass

@dataclass
class SchoolSubjectsModel(db.Model):
    school_subject_id:int = Column(Integer,primary_key=True)
    school_subject:str = Column(String(255),nullable=False)
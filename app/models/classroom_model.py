from app.configs.database import db
from sqlalchemy import Column,Integer,String
from dataclasses import dataclass

@dataclass
class ClassroomModel(db.Model):
    classroom:int = Column(Integer,primary_key=True)
    name:str = Column(String(255),nullable=False)
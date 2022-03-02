from app.configs.database import db
from sqlalchemy import Column,Integer,String
from dataclasses import dataclass
from uuid import uuid4
from sqlalchemy.dialects.postgresql import UUID

@dataclass
class ClassroomModel(db.Model):
    __tablename__="classrooms"
    classroom_id:str = Column(UUID(as_uuid=True),primary_key=True, default=uuid4)
    name:str = Column(String(255),nullable=False)
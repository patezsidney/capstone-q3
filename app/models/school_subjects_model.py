from app.configs.database import db
from sqlalchemy import Column,String
from dataclasses import dataclass
from uuid import uuid4
from sqlalchemy.dialects.postgresql import UUID

@dataclass
class SchoolSubjectsModel(db.Model):
    school_subject_id:str = Column(UUID(as_uuid=True),primary_key=True,default=uuid4)
    school_subject:str = Column(String(255),nullable=False)
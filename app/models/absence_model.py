from dataclasses import dataclass
from sqlalchemy import Column, Date, Boolean, Integer
from uuid import uuid4
from sqlalchemy.dialects.postgresql import UUID
from app.configs.database import db

@dataclass
class AbsenceModel(db.Model):
    __tablename__ = "absence"

    absence_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    date:str = Column(Date)
    justtify:bool = Column(Boolean, default=False)
    # classrom_id:str = Column(Integer, ForeignKey("classrom.id"), nullable=False)
    # student_id = Column(Integer, ForeignKey("student.id"), nullable=False)

from dataclasses import dataclass
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship,backref
from app.configs.database import db

from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4

@dataclass
class BooksModel(db.Model):

    book_id: str
    title: str
    author: str
    quantity: int

    __tablename__ = "books"

    book_id: str = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    title: str = Column(String(255), nullable=False)
    author: str = Column(String(255), nullable=False)
    quantity: int = Column(Integer)
from dataclasses import dataclass
from uuid import uuid4

from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import backref, relationship

from app.configs.database import db


@dataclass
class BooksModel(db.Model):

    __tablename__ = "books"

    book_id: str = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    title: str = Column(String(255), nullable=False)
    author: str = Column(String(255), nullable=False)
    quantity: int = Column(Integer)
from dataclasses import dataclass
from uuid import uuid4

from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import backref, relationship

from app.configs.database import db
from app.models.exc import IncorrectKeyError, MissingKeyError


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

    @classmethod
    def check_incorrect_keys(cls,data):
        key_error = [key for key in data.keys() if key not in ["title","author","quantity"]]

        if len(key_error) > 0:
            raise IncorrectKeyError
        
        return True

    @classmethod
    def missing_key(cls,data):
        key_error = [key for key in ["title","author"] if key not in data.keys()]

        if len(key_error) > 0:
            raise MissingKeyError
        
        return True
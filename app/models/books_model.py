from dataclasses import dataclass
from sqlalchemy import Column, String, Integer
from app.configs.database import db

@dataclass
class BooksModel(db.Model):

    __tablename__ = "books"

    book_id: str = Column(String, primary_key=True)
    title: str = Column(String(255), nullable=False)
    author: str = Column(String(255), nullable=False)
    quantity: int = Column(Integer)


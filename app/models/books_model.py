from sqlalchemy import Column, String, Integer
from app.configs.database import db


class BooksModel(db.Model):

    __tablename__ = "books"

    book_id = Column(String, primary_key=True)
    title = Column(String(255), nullable=False)
    author = Column(String(255), nullable=False)
    quantity = Column(Integer)


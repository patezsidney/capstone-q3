from http import HTTPStatus
from sqlalchemy.exc import DataError
from flask import jsonify
from app.models.books_model import BooksModel

def create_book():
    pass

def update_book(id: str):
    pass

def delete_book(id: str):
    pass

def get_book_list():
    pass

def get_book(book_id: str):
    try:
        book: BooksModel = BooksModel.query.get(book_id)
    
        return jsonify(book), HTTPStatus.OK
    
    except DataError:
        return {"msg": "Book not found"}, HTTPStatus.NOT_FOUND
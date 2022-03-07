from http import HTTPStatus
from sqlalchemy.orm.session import Session
from app.configs.database import db
from sqlalchemy.exc import DataError
from flask import jsonify
from app.models.library_model import LibraryModel


def create_book():
    pass

def update_book(id: str):
    pass

def delete_book(id: str):
    pass

def get_book_list():
    session: Session = db.session
    data = session.query(LibraryModel).all()

    return jsonify(data), HTTPStatus.OK

def get_book(book_id: str):
    try:
        book: LibraryModel = LibraryModel.query.get(book_id)
    
        return jsonify(book), HTTPStatus.OK
    
    except DataError:
        return {"msg": "Book not found"}, HTTPStatus.NOT_FOUND
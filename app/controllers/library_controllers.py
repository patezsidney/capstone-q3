from http import HTTPStatus

from flask import jsonify
from sqlalchemy.exc import DataError
from sqlalchemy.orm.session import Session

from app.configs.database import db
from app.models.library_model import LibraryModel


def create_library():
    pass

def update_library(id: str):
    pass

def delete_library(id: str):
    pass

def get_library_list():
    session: Session = db.session
    data = session.query(LibraryModel).paginate(page=None,per_page=20)

    return jsonify(data.items), HTTPStatus.OK

def get_library(book_id: str):
    try:
        book: LibraryModel = LibraryModel.query.get(book_id)
    
        return jsonify(book), HTTPStatus.OK
    
    except DataError:
        return {"msg": "Book not found"}, HTTPStatus.NOT_FOUND
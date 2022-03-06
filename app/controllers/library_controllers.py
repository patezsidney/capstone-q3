from http import HTTPStatus

from flask import jsonify
from app.models.library_model import LibraryModel
from sqlalchemy.orm.session import Session

from app.configs.database import db

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

def get_book(id: str):
    pass
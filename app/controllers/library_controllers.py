from http import HTTPStatus

from flask import current_app, jsonify, request
from sqlalchemy.exc import DataError
from sqlalchemy.orm.session import Session

from app.configs.auth import auth_employee
from app.configs.database import db
from app.models.exc import IncorrectKeyError, MissingKeyError
from app.models.library_model import LibraryModel


# @auth_employee.login_required(role=['admin','librarian'])
def library_register():
    try:
        data = request.get_json()

        LibraryModel.check_incorrect_keys(data)
        LibraryModel.missing_key(data)

        rent = LibraryModel(**data)

        current_app.db.session.add(rent)
        current_app.db.session.commit()
        
        return jsonify(rent),HTTPStatus.CREATED
    except IncorrectKeyError:
        return {"msg":"Incorrect key use"},HTTPStatus.BAD_REQUEST
    except MissingKeyError:
        return {"msg":"Missing key"},HTTPStatus.BAD_REQUEST

def update_library(id: str):
    pass

def delete_library(id: str):
    pass

def get_library_list():
    session: Session = db.session
    data = session.query(LibraryModel).all()

    return jsonify(data), HTTPStatus.OK

def get_library(book_id: str):
    try:
        book: LibraryModel = LibraryModel.query.get(book_id)
    
        return jsonify(book), HTTPStatus.OK
    
    except DataError:
        return {"msg": "Book not found"}, HTTPStatus.NOT_FOUND
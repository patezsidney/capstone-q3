from datetime import datetime
from http import HTTPStatus

from flask import current_app, jsonify, request
from sqlalchemy.exc import DataError
from sqlalchemy.orm.session import Session
from werkzeug.exceptions import NotFound

from app.configs.auth import auth_employee
from app.configs.database import db
from app.models.exc import IncorrectKeyError, MissingKeyError, TypeValueError
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

# @auth_employee.login_required(["librarian","admin"])
def edit_book_or_student_in_book_rental_by_id(id: str):
    try:
        data = request.get_json()
        LibraryModel.check_key_in_edit_book_or_student_in_rental(data)
        LibraryModel.check_type_value(data)

        rental = LibraryModel.query.filter_by(library_id=id).first()

        if rental == None:
            raise NotFound

        for key,value in data.items():
            setattr(rental,key,value)

        current_app.db.session.add(rental)
        current_app.db.session.commit()

        return jsonify(data),HTTPStatus.OK
    except IncorrectKeyError:
        return {"msg":"Incorrect key use"},HTTPStatus.BAD_REQUEST
    except TypeValueError:
        return {"msg":"request with incorrect value type!"},HTTPStatus.BAD_REQUEST
    except NotFound:
        return {"msg":"rental not found"},HTTPStatus.NOT_FOUND

# @auth_employee.login_required(["admin","librarian"])
def register_book_rental_return_by_id(id:str):
    try:
        data = request.get_json()
        LibraryModel.check_incorrect_keys(data)
        LibraryModel.check_type_value(data)

        data["date_return"]=datetime.now()

        rental = LibraryModel.query.filter_by(library_id=id).first()

        if rental == None:
            raise NotFound

        for key,value in data.items():
            setattr(rental,key,value)

        current_app.db.session.add(rental)
        current_app.db.session.commit()

        return jsonify(data),HTTPStatus.OK
    except IncorrectKeyError:
        return {"msg":"Incorrect key use"},HTTPStatus.BAD_REQUEST
    except TypeValueError:
        return {"msg":"request with incorrect value type!"},HTTPStatus.BAD_REQUEST
    except NotFound:
        return {"msg":"rental not found"},HTTPStatus.NOT_FOUND

# @auth_employee.login_required(role="admin")
def delete_library(library_id: str):
    
    try:
        library: LibraryModel = LibraryModel.query.get(library_id)
    
        db.session.delete(library)
        db.session.commit()

        return {}, HTTPStatus.NO_CONTENT
    
    except DataError:
        return {"mgs": "library_id not found"}, HTTPStatus.NOT_FOUND

def get_library_list():
    session: Session = db.session
    data = session.query(LibraryModel).all().paginate(page=None,per_page=20)

    return jsonify(data), HTTPStatus.OK

def get_library(book_id: str):
    try:
        book: LibraryModel = LibraryModel.query.get(book_id).paginate(page=None,per_page=20)
    
        return jsonify(book), HTTPStatus.OK
    
    except DataError:
        return {"msg": "Book not found"}, HTTPStatus.NOT_FOUND
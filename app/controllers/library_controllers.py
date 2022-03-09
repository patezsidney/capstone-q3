from http import HTTPStatus

from flask import current_app, jsonify, request
from sqlalchemy import null
from sqlalchemy.exc import DataError
from sqlalchemy.orm.session import Session
from werkzeug.exceptions import NotFound
from sqlalchemy.orm import Query

from app.configs.auth import auth_employee
from app.configs.database import db
from app.models.exc import IncorrectKeyError, MissingKeyError
from app.models.library_model import LibraryModel
from app.models.students_model import StudentsModel


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
    data = session.query(LibraryModel).all()

    return jsonify(data), HTTPStatus.OK

def get_library(book_id: str):
    try:
        book: LibraryModel = LibraryModel.query.get(book_id)
    
        return jsonify(book), HTTPStatus.OK
    
    except DataError:
        return {"msg": "Book not found"}, HTTPStatus.NOT_FOUND

def student_get_rented_books_by_id(id:str):
    try:
        books = LibraryModel.query.filter_by(student_id=id).paginate(page=None,per_page=20)
   
        if books == None:
            raise NotFound

        if not len(books):
            return {"msg":"You don't have any books to rent"}

        else:
            return jsonify(books.items),HTTPStatus.OK
    except NotFound:
        return {"msg":"No student records"},HTTPStatus.NOT_FOUND
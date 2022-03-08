from http import HTTPStatus

from flask import current_app, jsonify, request
from werkzeug.exceptions import NotFound

from app.configs.auth import auth_employee
from app.configs.database import db
from app.models.books_model import BooksModel
from app.models.exc import IncorrectKeyError, MissingKeyError


# @auth_employee.login_required(role=["librarian","admin"])
def patch_book_by_id(book_id):
    try:
        data = request.get_json()

        book = BooksModel.query.filter_by(book_id=book_id).first()

        if book == None:
            raise NotFound

        for key, value in data.items():
            setattr(book,key,value)
            
        return data, HTTPStatus.OK
    except NotFound:
        return {"msg":"book not found"},HTTPStatus.NOT_FOUND

        

# @auth_employee.login_required(role=['librarian','admin'])
def register_books():
    try:
        data = request.get_json()

        BooksModel.check_incorrect_keys(data)
        BooksModel.missing_key(data)

        book = BooksModel(**data)

        current_app.db.session.add(book)
        current_app.db.session.commit()

        return jsonify(book),HTTPStatus.CREATED
    except IncorrectKeyError:
        return {"msg":"Incorrect key use"},HTTPStatus.BAD_REQUEST
    except MissingKeyError:
        return {"msg":"Missing key in request"},HTTPStatus.BAD_REQUEST

# @auth_employee.login_required(role="admin")
def delete_book_by_id(book_id):
    try:
        book = BooksModel.query.filter_by(book_id=book_id).first()

        if book == None:
            raise NotFound
        
        current_app.db.session.delete(book)
        current_app.db.session.commit()

        return "",HTTPStatus.OK
    except NotFound:
        return {"msg":"Book not found!"},HTTPStatus.NOT_FOUND

def get_all_books():
    
    books: BooksModel = db.session.query(BooksModel).all()

    return jsonify(books), HTTPStatus.OK
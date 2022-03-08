from flask import current_app
from app.models.books_model import BooksModel
from http import HTTPStatus
from app.configs.auth import auth_employee
from werkzeug.exceptions import NotFound

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

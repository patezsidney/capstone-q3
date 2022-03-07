from flask import Blueprint

from app.controllers import books_controllers

bp = Blueprint('books', __name__, url_prefix='/books')

bp.get('/<book_id>')(books_controllers.get_book)
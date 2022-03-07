from flask import Blueprint

from app.controllers import library_controllers

bp = Blueprint('library', __name__, url_prefix='/library')

bp.get("")(library_controllers.get_book_list)

bp.get('/<book_id>')(library_controllers.get_book)


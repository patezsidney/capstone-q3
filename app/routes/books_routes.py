from flask import Blueprint
from app.controllers import books_controllers

bp = Blueprint("books",__name__,url_prefix="/books")
                                                                     
bp.patch("/<book_id>")(books_controllers.patch_book_by_id)
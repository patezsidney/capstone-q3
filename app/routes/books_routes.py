from flask import Blueprint
from app.controllers import books_controllers

bp = Blueprint("books",__name__,url_prefix="/books")
                                                                     
bp.delete("/<book_id>")(books_controllers.delete_book_by_id)
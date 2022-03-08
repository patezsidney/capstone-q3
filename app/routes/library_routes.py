from flask import Blueprint

from app.controllers import library_controllers

bp = Blueprint('library', __name__, url_prefix='/library')

bp.get("")(library_controllers.get_library_list)
bp.get('/<library_id>')(library_controllers.get_library)
bp.post("/rental")(library_controllers.library_register)


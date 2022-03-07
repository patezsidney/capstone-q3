from flask import Blueprint

from app.controllers import rental_controllers

bp = Blueprint('rents', __name__, url_prefix='/rents')


bp.get('/<rental_id>')(rental_controllers.get_rental_by_id)
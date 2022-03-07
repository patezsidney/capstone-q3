from flask import Blueprint

from app.controllers import absense_controllers

bp = Blueprint("absence", __name__, url_prefix="/absence")

bp.delete("/<absence_id>")(absense_controllers.delete_absense)
from flask import Blueprint

from app.controllers import absense_controllers

bp = Blueprint('absences', __name__, url_prefix='/absences')

bp.get("/<student_id>")(absense_controllers.get_student_absense)
bp.patch("/<absence_id>")(absense_controllers.update_absense)
bp.delete("/<absence_id>")(absense_controllers.delete_absense)

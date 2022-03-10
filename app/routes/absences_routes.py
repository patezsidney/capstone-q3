from flask import Blueprint

from app.controllers import absense_controllers

bp = Blueprint('absences', __name__, url_prefix='/absences')

bp.post("")(absense_controllers.create_absense)
bp.get("/<student_id>")(absense_controllers.get_student_absense)
bp.get("")(absense_controllers.get_all_absense)
bp.patch("/<absence_id>")(absense_controllers.update_absense)
bp.delete("/<absence_id>")(absense_controllers.delete_absense)

bp.get("/student")(absense_controllers.get_student_absence_by_api_key)
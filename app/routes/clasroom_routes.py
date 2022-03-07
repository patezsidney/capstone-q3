from flask import Blueprint

from app.controllers import classroom_controllers

bp = Blueprint("classrooms", __name__, url_prefix="/classrooms")

bp.post("")(classroom_controllers.create_classroom)
bp.get("")(classroom_controllers.get_all_classroom)
bp.get("/<classroom_id>")(classroom_controllers.get_employee_classroom)
bp.delete("/<classroom_id>")(classroom_controllers.delete_classroom)
bp.patch("/<classroom_id>")(classroom_controllers.update_classroom)

from http import HTTPStatus
from flask import Blueprint

from app.controllers import employees_controllers

bp = Blueprint("employees", __name__, url_prefix="/employees")

bp.post("")(employees_controllers.create_employee)
bp.get("")(employees_controllers.get_all_employees)
bp.patch("/<employee_id>")(employees_controllers.update_employee)
bp.delete("/<employee_id>")(employees_controllers.delete_employee)
bp.get("/<employee_id>")(employees_controllers.get_employee_by_id)
bp.post("login")(employees_controllers.sigin)

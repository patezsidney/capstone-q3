from flask import Blueprint

from app.controllers import employees_controllers

bp = Blueprint("employees", __name__, url_prefix="/employees")

bp.post("")(employees_controllers.create_employee)
bp.get("")(employees_controllers.get_all_employees)
bp.post("login")(employees_controllers.sigin)
from flask import Blueprint

from app.controllers import absense_controllers

bp = Blueprint('absences', __name__, url_prefix='/absences')

bp.get("/<student_id>")(absense_controllers.get_student_absense)
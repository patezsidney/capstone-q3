from flask import Blueprint

from app.controllers import school_subjects_controllers

bp = Blueprint('school_subjects', __name__, url_prefix='/school_subjects')

bp.post("/register")(school_subjects_controllers.register_teacher_in_school_subject)
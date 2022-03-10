from flask import Blueprint

from app.controllers import school_subjects_controllers

bp = Blueprint('school_subjects', __name__, url_prefix='/school_subjects')

bp.post("/register")(school_subjects_controllers.register_teacher_in_school_subject)
bp.patch("/edit/<school_subject_id>")(school_subjects_controllers.edit_school_subject_by_id)
bp.delete("/<school_subject_id>")(school_subjects_controllers.delete_school_subjects)
bp.get("")(school_subjects_controllers.get_all_school_subjects)
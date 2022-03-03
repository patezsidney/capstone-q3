from http import HTTPStatus

from flask import jsonify


def get_example_controller():
    return jsonify({"msg": "Success example"}), HTTPStatus.OK
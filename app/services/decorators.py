from functools import wraps
from flask import request
from http import HTTPStatus

def verify_some_keys(trusted_keys: "list[str]"):
    def test_key(func):
        @wraps(func)
        def wraped_function(employee_id):
            try:
                data = request.get_json()
                for key in data.keys():
                    if key not in trusted_keys:
                        print(key)
                        raise KeyError
                return func(employee_id)
            except KeyError:
                return {
                        "error": "incorrect key(s)",
                        "expected to be in": trusted_keys,
                        "received": list(data.keys())
                        }, HTTPStatus.UNPROCESSABLE_ENTITY
        return wraped_function
    return test_key
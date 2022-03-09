from functools import wraps
from http import HTTPStatus

from flask import request


def verify_some_keys(trusted_keys: "list[str]"):
    def test_key(func):
        @wraps(func)
        def wraped_function(*args, **kargs):
            try:
                data = request.get_json()
                for key in data.keys():
                    if key not in trusted_keys:
                        raise KeyError
                return func(*args, **kargs)
            except KeyError:
                return {
                        "error": "incorrect key(s)",
                        "expected to be in": trusted_keys,
                        "received": list(data.keys())
                        }, HTTPStatus.BAD_REQUEST
        return wraped_function
    return test_key

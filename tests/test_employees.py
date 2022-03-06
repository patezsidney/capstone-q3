import re
from flask import request
from flask.testing import FlaskClient

def test_create_employee(client: FlaskClient):
    request_data = {
        "name": "Jhon Doe",
        "email": "jhondoe1@mail.com",
        "wage": 3020.90,
        "access_level": "admin",
        "password": "1234"
    }
    expected_keys = ["name", "employee_id", "email", "wage", "access_level"]
    expected_keys.sort()
    

    request_response = client.post("/api/employees", json=request_data, follow_redirects=True )
    response_json: dict = request_response.get_json()
    response_keys = list(response_json.keys())
    response_keys.sort()

    assert (response_keys == expected_keys), "verifique as keys retornadas"
    assert (type(response_json) is dict), "Verificar se está retornando um dict"
    assert (request_response.status_code == 201), "Verificar se o status code é created"


def test_get_all_employees(client):
    request_response = client.get("/api/employees")

    assert (request_response.status_code == 200), "Verificar se o status code é ok"

def test_login_employee_success(client):
    request_register_data = {
        "name": "Renato",
        "email": "renato@mail.com",
        "wage": 2000.00,
        "password": "1234",
        "access_level": "employee"
    }

    request_register_response = client.post("/api/employees", json=request_register_data, follow_redirects=True )
    response_register_json: dict = request_register_response.get_json()
    request_login_data = {
        "employee_id": response_register_json["employee_id"], 
	    "password": request_register_data["password"]
    }

    request_login_response = client.post("/api/employees/login", json=request_login_data, follow_redirects=True )

    assert( request_login_response.get_json().get("api_key")), "Verificar se retornou a api_key"
    assert (request_login_response.status_code == 200), "Verificar se o status code é OK"

def test_login_employee_error_password(client):
    request_register_data = {
        "name": "Renato2",
        "email": "renato2@mail.com",
        "wage": 2000.00,
        "password": "1234",
        "access_level": "employee"
    }

    request_register_response = client.post("/api/employees", json=request_register_data, follow_redirects=True )
    response_register_json: dict = request_register_response.get_json()
    request_login_data = {
        "employee_id": "1234312412", 
	    "password": request_register_data["password"]
    }

    request_login_response = client.post("/api/employees/login", json=request_login_data, follow_redirects=True )

    assert( request_login_response.get_json().get("msg") == "Invalid employee id"), "Verificar se retornou a mensagem correta"
    assert(request_login_response.status_code == 401), "Verificar se o status code é Unauthorized"

def test_login_employee_error_id(client):
    request_register_data = {
        "name": "Renato3",
        "email": "renato3@mail.com",
        "wage": 2000.00,
        "password": "1234",
        "access_level": "employee"
    }

    request_register_response = client.post("/api/employees", json=request_register_data, follow_redirects=True )
    response_register_json: dict = request_register_response.get_json()
    request_login_data = {
        "employee_id": response_register_json["employee_id"], 
	    "password": "123"
    }

    request_login_response = client.post("/api/employees/login", json=request_login_data, follow_redirects=True )

    assert(request_login_response.get_json().get("msg") == "Wrong password"), "Verificar se retornou a mensagem correta"
    assert(request_login_response.status_code == 401), "Verificar se o status code é Unauthorized"
    


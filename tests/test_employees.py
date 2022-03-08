import re

from flask import request
from flask.testing import FlaskClient

from app.models.employee_model import EmployeeModel


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


def test_patch_employee_success(client: FlaskClient):
    request_data = {
        "name": "Jhon",
        "email": "jhon@mail.com",
        "wage": 3020.90,
        "access_level": "admin",
        "password": "1234"
    }

    patch_data = {
        "name": "Jhona",
        "email": "jhona@mail.com",
    }

    request_response = client.post("/api/employees", json=request_data, follow_redirects=True )
    response_json: dict = request_response.get_json()

    patch_response = client.patch(f"/api/employees/{response_json['employee_id']}", json=patch_data, follow_redirects=True )
    patch_json: dict = patch_response.get_json()
    

    assert (patch_json['name'] == patch_data['name']), "verifique se o nome foi retornado correto"
    assert (patch_response.status_code == 200), "Verificar se o status code é OK"

def test_patch_employee_error_conflict(client: FlaskClient):
    request_data = {
        "name": "Jhon",
        "email": "jhon@mail.com",
        "wage": 3020.90,
        "access_level": "admin",
        "password": "1234"
    }
    request_data2 = {
        "name": "Jhono",
        "email": "jhono@mail.com",
        "wage": 3020.90,
        "access_level": "admin",
        "password": "1234"
    }
    patch_data = {
        "name": "Jhon",
        "email": "jhon@mail.com",
    }

    client.post("/api/employees", json=request_data, follow_redirects=True )
    request_response = client.post("/api/employees", json=request_data2, follow_redirects=True )
    response_json: dict = request_response.get_json()

    patch_response = client.patch(f"/api/employees/{response_json['employee_id']}", json=patch_data, follow_redirects=True )
    patch_json: dict = patch_response.get_json()

    assert (patch_response.status_code == 409), "Verificar se o status code é Conflict"

def test_patch_employee_error_wrong_key(client: FlaskClient):
    request_data = {
        "name": "Jhon",
        "email": "jhon@mail.com",
        "wage": 3020.90,
        "access_level": "admin",
        "password": "1234"
    }

    patch_data = {
        "names": "Jhon",
    }

    request_response = client.post("/api/employees", json=request_data, follow_redirects=True )
    response_json: dict = request_response.get_json()

    patch_response = client.patch(f"/api/employees/{response_json['employee_id']}", json=patch_data, follow_redirects=True )
    patch_json: dict = patch_response.get_json()

    assert (patch_response.status_code == 422), "Verificar se o status code é UNPROCESSABLE_ENTITY"

def test_delete_success(client):
    request_data = {
        "name": "Jhon Doe5",
        "email": "jhondoe5@mail.com",
        "wage": 3020.90,
        "access_level": "admin",
        "password": "1234"
    }
    request_response = client.post("/api/employees", json=request_data, follow_redirects=True )
    response_json: dict = request_response.get_json()

    request_delete = client.delete(f"/api/employees/{response_json['employee_id']}")

    assert (request_delete.status_code == 204), "Verificar se o status code é No Content"

def test_delete_error(client):

    request_delete = client.delete(f"/api/employees/b3298cfc-7fb8-47af-91ed-f2d8c4545c3d")

    assert (request_delete.status_code == 404), "Verificar se o status code é Not Found"


def test_get_employee_error(client: FlaskClient):
    request_data = {
        "name": "Jhon Doe2",
        "email": "jhondoe12@mail.com",
        "wage": 3020.90,
        "access_level": "admin",
        "password": "1234",
        "api_key": "7VyrFqAJeDa-EOBK457GsQ"
    }    
    request_response = client.post("/api/employees", json=request_data, follow_redirects=True )
    response_json: dict = request_response.get_json()

    request_response_get = client.get(f"/api/employees/{response_json['employee_id']}", json=request_data, follow_redirects=True)
    response_get_json: dict = request_response_get.get_json()

    assert (request_response_get.status_code == 401), "Verificar se o status code é 401"

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


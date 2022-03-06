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
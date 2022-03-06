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

    request_delete = client.delete(f"/api/employees/b3298cfc-7fb8-47af-91ed-f2d8c4545cdd")

    assert (request_delete.status_code == 404), "Verificar se o status code é Not Found"
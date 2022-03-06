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
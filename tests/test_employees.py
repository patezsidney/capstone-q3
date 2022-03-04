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
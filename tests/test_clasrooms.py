from flask.testing import FlaskClient

def test_get_all_classrooms(client):
    request_response = client.get("/api/classrooms")

    assert (request_response.status_code == 200), "Verificar se o status code é ok"

def test_create_classroom(client: FlaskClient):
    request_data = {
        "name": "1C"
    }
    expected_keys = ["name", "classroom_id"]
    expected_keys.sort()
    
    request_response = client.post("/api/classrooms", json=request_data, follow_redirects=True )
    response_json: dict = request_response.get_json()
    response_keys = list(response_json.keys())
    response_keys.sort()

    assert (response_keys == expected_keys), "verifique as keys retornadas"
    assert (type(response_json) is dict), "Verificar se está retornando um dict"
    assert (request_response.status_code == 201), "Verificar se o status code é created"

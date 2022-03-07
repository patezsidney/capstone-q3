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

def test_delete_success(client):
    request_data = {
        "name": "2B"
    }

    request_response = client.post("/api/classrooms", json=request_data, follow_redirects=True )
    response_json: dict = request_response.get_json()

    request_delete = client.delete(f"/api/classrooms/{response_json['classroom_id']}")

    assert (request_delete.status_code == 204), "Verificar se o status code é No Content"

def test_delete_error(client):

    request_delete = client.delete(f"/api/classrooms/b3298cfc-7fb8-47af-91ed-f2d8c4545cdd")

    assert (request_delete.status_code == 404), "Verificar se o status code é Not Found"


def test_patch_classroom_success(client: FlaskClient):
    request_data = {
        "name": "3T",
    }

    patch_data = {
        "name": "3A",
    }

    request_response = client.post("/api/classrooms", json=request_data, follow_redirects=True )
    response_json: dict = request_response.get_json()

    patch_response = client.patch(f"/api/classrooms/{response_json['classroom_id']}", json=patch_data, follow_redirects=True )
    patch_json: dict = patch_response.get_json()
    

    assert (patch_json['name'] == patch_data['name']), "verifique se o nome foi retornado correto"
    assert (patch_response.status_code == 200), "Verificar se o status code é OK"

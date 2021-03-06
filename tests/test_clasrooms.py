from email import header

from flask.testing import FlaskClient


def test_get_all_classrooms(client):
    headers = {"Authorization": "Bearer 1234"}
    request_response = client.get("/api/classrooms", headers=headers)

    assert (request_response.status_code == 200), "Verificar se o status code é ok"

def test_create_classroom(client: FlaskClient):
    request_data = {
        "name": "1C"
    }
    headers = {"Authorization": "Bearer 1234"}
    expected_keys = ["name", "classroom_id"]
    expected_keys.sort()
    
    request_response = client.post("/api/classrooms", json=request_data, follow_redirects=True, headers=headers )
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

    headers = {"Authorization": "Bearer 1234"}

    request_response = client.post("/api/classrooms", json=request_data, follow_redirects=True, headers=headers )
    response_json: dict = request_response.get_json()

    request_delete = client.delete(f"/api/classrooms/{response_json['classroom_id']}", headers=headers)

    assert (request_delete.status_code == 204), "Verificar se o status code é No Content"

def test_delete_error(client):
    headers = {"Authorization": "Bearer 1234"}
    request_delete = client.delete(f"/api/classrooms/b3298cfc-7fb8-47af-91ed-f2d8c4545cdd", headers=headers)

    assert (request_delete.status_code == 404), "Verificar se o status code é Not Found"


def test_patch_classroom_success(client: FlaskClient):
    request_data = {
        "name": "3T",
    }

    patch_data = {
        "name": "3A",
    }
    headers = {"Authorization": "Bearer 1234"}
    request_response = client.post("/api/classrooms", json=request_data, follow_redirects=True, headers=headers )
    response_json: dict = request_response.get_json()

    patch_response = client.patch(f"/api/classrooms/{response_json['classroom_id']}", json=patch_data, follow_redirects=True, headers=headers )
    patch_json: dict = patch_response.get_json()
    

    assert (patch_json['name'] == patch_data['name']), "verifique se o nome foi retornado correto"
    assert (patch_response.status_code == 202), "Verificar se o status code é OK"

def test_get_on_classroom_success(client: FlaskClient):
    headers = {"Authorization": "Bearer 1234"}

    expected_keys = ["name", "classroom_id", "school_subjects", "students", "teacher"]
    expected_keys.sort()
    
    request_response_get = client.get(f"/api/classrooms/51df51e0-00a7-49e3-9f2e-0405574f5c20", headers=headers )

    response_json_get: dict = request_response_get.get_json()
    response_keys = list(response_json_get[0].keys())
    response_keys.sort()

    assert (response_keys == expected_keys), "verifique as keys retornadas"
    assert (request_response_get.status_code == 200), "Verificar se o status code é OK"


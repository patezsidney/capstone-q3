from flask.testing import FlaskClient
headers = {"Authorization": "Bearer 1234"}

def test_patch_student_by_id(client: FlaskClient):

    request_data = {
        "contact_name":"Magnus Carlsen",
        "contact_email":"student02@mail.com"
    }    
    
    request_response = client.patch("/api/students/51df51e0-00a7-49e3-9f2e-0405574f5c20",json=request_data, heades=headers)
    
    assert (request_response.status_code == 202), "Verificar se o status code é ACCEPTED"

def test_patch_student_with_invalid_key(client: FlaskClient):

    request_data = {
        "contact":"Magnus Carlsen",
        "contact_email":"student02@mail.com"
    }    
    
    request_response = client.patch("/api/students/51df51e0-00a7-49e3-9f2e-0405574f5c20",json=request_data, headers=headers)
    
    assert (request_response.status_code == 400), "Verificar se o status code é BAD REQUEST"

def test_patch_student_with_invalid_id(client: FlaskClient):

    request_data = {
        "contact_name":"Magnus Carlsen",
        "contact_email":"student02@mail.com"
    }    
    
    request_response = client.patch("/api/students/51df51e0-00a7-49e3-9f2e-0405574f5c55",json=request_data, headers=headers)
    
    assert (request_response.status_code == 404), "Verificar se o status code é NOT FOUND"

def test_patch_student_with_incorrect_type_value(client: FlaskClient):

    request_data = {
        "contact_name":"Magnus Carlsen",
        "cpf": 00000000000
    }    
    
    request_response = client.patch("/api/students/51df51e0-00a7-49e3-9f2e-0405574f5c20",json=request_data, headers=headers)
    
    assert (request_response.status_code == 400), "Verificar se o status code é BAD REQUEST"

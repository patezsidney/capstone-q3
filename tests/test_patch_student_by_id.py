from flask.testing import FlaskClient


def test_patch_student_by_id(client: FlaskClient):

    request_data = {
        "contact_name":"Magnus Carlsen",
        "contact_email":"student02@mail.com"
    }    
    
    request_response = client.patch("/api/students/51df51e0-00a7-49e3-9f2e-0405574f5c20",json=request_data)
    
    assert (request_response.status_code == 200), "Verificar se o status code é OK"

def test_patch_student_with_invalid_key(client: FlaskClient):

    request_data = {
        "contact":"Magnus Carlsen",
        "contact_email":"student02@mail.com"
    }    
    
    request_response = client.patch("/api/students/51df51e0-00a7-49e3-9f2e-0405574f5c20",json=request_data)
    
    assert (request_response.status_code == 409), "Verificar se o status code é OK"
from flask.testing import FlaskClient
headers = {"Authorization": "Bearer 1234"}


def test_del_student_by_id(client: FlaskClient): 
    
    request_response = client.delete("/api/students/1d5225ef-5638-4397-9989-e604a2cceca0", headers=headers)

    print(request_response)
    
    assert (request_response.status_code == 200), "Verificar se o status code é OK"

def test_del_student_with_ivld_key(client: FlaskClient):
    
    request_response = client.patch("/api/students/51df51e0-00a7-49e3-9f", headers=headers)
    
    assert (request_response.status_code == 404), "Verificar se o status code é OK"

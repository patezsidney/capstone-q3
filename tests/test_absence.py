from flask.testing import FlaskClient

def test_create_absence(client: FlaskClient):
    
    request_data = {
        "absence_id": 'b20dfcbb-f121-41ef-bf96-cb988d333333',
        "date": "Sat, 15 Feb 2020 00:00:00 GMT",
        "justify": True,
        "classroom_id": '51df51e0-00a7-49e3-9f2e-0405574f5c20',
        "student_id": '1d5225ef-5638-4397-9989-e604a2cceca0'
    }

    response = client.post("/api/absences", json=request_data, follow_redirects=True)

    assert (response.status_code == 201), "Verificar o status code"


def test_delete_absence_success(client: FlaskClient):
    request_data = {
        "date": "Sat, 15 Feb 2020 00:00:00 GMT",
        "justify": True,
        "classroom_id": '51df51e0-00a7-49e3-9f2e-0405574f5c20',
        "student_id": '1d5225ef-5638-4397-9989-e604a2cceca0'
    }

    request_response = client.post("/api/absences", json=request_data, follow_redirects=True )
    response_json: dict = request_response.get_json()

    request_delete = client.delete(f"/api/absences/{response_json['absence_id']}")

    assert (request_delete.status_code == 204), "Verificar se o status code é No Content"


def test_delete_absence_error(client: FlaskClient):

    request_delete = client.delete(f"/api/absences/b3298cfc-7fb8-47af-91ed-f2d8c4545cdd")

    assert (request_delete.status_code == 404), "Verificar se o status code é Not Found"



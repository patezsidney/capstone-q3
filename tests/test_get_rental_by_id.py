from flask.testing import FlaskClient

def test_rental_by_id(client: FlaskClient):
    response = client.get("/api/rents/3554e9f0-8208-4e99-81c1-d79f3caf891c")
    mock_reponse = {
                    "rental": {
                    "library_id": "3554e9f0-8208-4e99-81c1-d79f3caf891c",
                    "date_withdrawal": "Sat, 01 Feb 2020 00:00:00 GMT",
                    "date_accurancy": "Sat, 15 Feb 2020 00:00:00 GMT",
                    "book_id": "2fc09626-8a2c-4ef7-b59d-4a56e77e5714",
                    "student_id": "51df51e0-00a7-49e3-9f2e-0405574f5c20",
                    "employee_id": "b3298cfc-7fb8-47af-91ed-f2d8c4545cdd",
                    "date_return": "Sat, 15 Feb 2020 00:00:00 GMT"
                    },
                    "student": "felipe",
                    "book": "Harry Potter - E a pedra filosofal",
                    "employee": "matheus"
                    }
    
    response_json: dict = response.get_json()
    
    assert(response_json == mock_reponse), "Verificar se o retorno está correto"
    assert (type(response_json) is dict), "Verificar se está retornando um dict"
    assert (response.status_code == 200), "Verificar se o status code é OK"
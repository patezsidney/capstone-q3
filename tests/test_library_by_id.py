from flask.testing import FlaskClient

# Alterei o dados da requisição do teste devido ao id que estava sendo usado, esta sendo deletado em um teste
# que acontece antes desse.

def test_get_library_by_id(client: FlaskClient):
    response = client.get("/api/library/3554e9f0-8208-4e99-81c1-d79f3caf891c",headers={"Authorization": "Bearer 1234"})

    # response = client.get("/api/library/3554e9f0-8208-4e99-81c1-d79f3caf891c")
    mock_reponse = {
                    "library": {
                        "library_id":'3554e9f0-8208-4e99-81c1-d79f3caf891c',
                        "date_accurancy": 'Sat, 15 Feb 2020 00:00:00 GMT',
                        "date_return": 'Sat, 15 Feb 2020 00:00:00 GMT',
                        "date_withdrawal": 'Sat, 01 Feb 2020 00:00:00 GMT',
                        "employee_id":'b3298cfc-7fb8-47af-91ed-f2d8c4545cdd',
                        "book_id":'2fc09626-8a2c-4ef7-b59d-4a56e77e5714',
                        "student_id":'51df51e0-00a7-49e3-9f2e-0405574f5c20'
                        },
                    "student": "felipe",
                    "book": "Harry Potter - E a pedra filosofal",
                    "employee": "matheus"
                    }
    
    response_json: dict = response.get_json()

    assert(response_json == mock_reponse), "Verificar se o retorno está correto"
    assert (type(response_json) is dict), "Verificar se está retornando um dict"
    assert (response.status_code == 200), "Verificar se o status code é OK"
from flask.testing import FlaskClient

# Alterei o dados da requisição do teste devido ao id que estava sendo usado, esta sendo deletado em um teste
# que acontece antes desse.

def test_get_library_by_id(client: FlaskClient):
    response = client.get("/api/library/23c3c4c8-d923-43d3-bc1b-c47d7b741ee1")

    # response = client.get("/api/library/3554e9f0-8208-4e99-81c1-d79f3caf891c")
    mock_reponse = {
                    "library": {
                        "library_id":'23c3c4c8-d923-43d3-bc1b-c47d7b741ee1',
                        "date_accurancy": 'Sat, 15 Feb 2020 00:00:00 GMT',
                        "date_return": 'Sat, 15 Feb 2020 00:00:00 GMT',
                        "date_withdrawal": 'Sat, 01 Feb 2020 00:00:00 GMT',
                        "employee_id":'b3298cfc-7fb8-47af-91ed-f2d8c4545cdd',
                        "book_id":'081c575b-a38f-4f41-bf15-2593cd58ab93',
                        "student_id":'7dc82c28-4766-4bff-829b-2198a2e1ef98'
                        },
                    "student": "rafael",
                    "book": "Harry Potter e a Câmara dos Segredos",
                    "employee": "matheus"
                    }
    
    response_json: dict = response.get_json()

    assert(response_json == mock_reponse), "Verificar se o retorno está correto"
    assert (type(response_json) is dict), "Verificar se está retornando um dict"
    assert (response.status_code == 200), "Verificar se o status code é OK"
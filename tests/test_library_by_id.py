from flask.testing import FlaskClient

# Alterei o dados da requisição do teste devido ao id que estava sendo usado, esta sendo deletado em um teste
# que acontece antes desse.

def test_get_library_by_id(client: FlaskClient):
    response = client.get("/api/library/23c3c4c8-d923-43d3-bc1b-c47d7b741ee1",headers={"Authorization": 'Bearer 1236'})

    mock_reponse = {
                    "library_id":'23c3c4c8-d923-43d3-bc1b-c47d7b741ee1',
                    "date_accurrancy": 'Sat, 15 Feb 2020 00:00:00 GMT',
                    "date_return": 'Sat, 15 Feb 2020 00:00:00 GMT',
                    "date_withdraw": 'Sat, 01 Feb 2020 00:00:00 GMT',
                    "student": "rafael",
                    "book": "Harry Potter e a Câmara dos Segredos",
                    "librarian": "matheus"
                    }
    
    response_json: dict = response.get_json()

    assert(response_json == mock_reponse), "Verificar se o retorno está correto"
    assert (type(response_json) is dict), "Verificar se está retornando um dict"
    assert (response.status_code == 200), "Verificar se o status code é OK"
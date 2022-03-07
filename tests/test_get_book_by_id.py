from flask.testing import FlaskClient

def test_get_library_by_id(client: FlaskClient):
    response = client.get("/api/books/2fc09626-8a2c-4ef7-b59d-4a56e77e5714")

    mock_reponse = {
                    "book_id": "2fc09626-8a2c-4ef7-b59d-4a56e77e5714",
                    "title": "Harry Potter - E a pedra filosofal",
                    "author": "J.K. Rowling",
                    "quantity": 5
                    }
    
    response_json: dict = response.get_json()

    assert(response_json == mock_reponse), "Verificar se o retorno está correto"
    assert (type(response_json) is dict), "Verificar se está retornando um dict"
    assert (response.status_code == 200), "Verificar se o status code é OK"
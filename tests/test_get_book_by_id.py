from flask.testing import FlaskClient


def test_get_book_by_id(client: FlaskClient):
    response = client.get("/api/books/081c575b-a38f-4f41-bf15-2593cd58ab93", headers={"Authorization": 'Bearer 1236'})
    mock_response = {
                    "title": "Harry Potter E A Câmara Dos Segredos",
                    "author": "J.K. Rowling",
                    "quantity": 3
                    }
    
    response_json = response.get_json()

    assert(response_json == mock_response), "Verificar se o retorno está correto"
    assert (type(response_json) is dict), "Verificar se está retornando um dict"
    assert (response.status_code == 200), "Verificar se o status code é OK"
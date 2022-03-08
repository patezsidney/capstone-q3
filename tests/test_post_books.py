from flask.testing import FlaskClient


def test_register_books(client: FlaskClient):

    request_data = {
        "title":"Conjurador",
        "author":"Taran Matharu",
        "quantity":1
    }    
    
    request_response = client.post("/api/books/register",json=request_data)
    
    assert (request_response.status_code == 201), "Verificar se o status code é OK"

def test_register_books_with_incorrect_key(client: FlaskClient):

    request_data = {
        "title":"EndGame Strategy",
        "author_name":"M.I. Shereshevsky"
    }    
    
    request_response = client.post("/api/books/register",json=request_data)
    
    assert (request_response.status_code == 400), "Verificar se o status code é BAD REQUEST"
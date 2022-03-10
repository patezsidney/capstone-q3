from flask.testing import FlaskClient


def test_patch_book_by_id(client: FlaskClient):

    request_data = {
        "title":"Harry Potter e a camâra secreta"
    }    
    
    request_response = client.patch('/api/books/081c575b-a38f-4f41-bf15-2593cd58ab93',json=request_data, headers={"Authorization": 'Bearer 1236'})
    
    assert (request_response.status_code == 200), 'Verificar se o status code é OK'

def test_patch_book_with_invalid_id(client: FlaskClient):

    request_data = {
        'title':'Harry Potter e a pedra filosofal'
    }   
    
    request_response = client.patch('/api/books/2fc09626-8a2c-4ef7-b59d-4a56e77e5719',json=request_data, headers={"Authorization": 'Bearer 1234'})

    assert (request_response.status_code == 404), 'Verificar se o status code é NOT FOUND'
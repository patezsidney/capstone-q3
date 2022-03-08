from flask.testing import FlaskClient


def test_patch_book_by_id(client: FlaskClient):

    request_data = {
        'title':'Harry Potter e a pedra filosofal'
    }    
    
    request_response = client.patch('/api/books/2fc09626-8a2c-4ef7-b59d-4a56e77e5714',json=request_data)
    
    assert (request_response.status_code == 200), 'Verificar se o status code é OK'

def test_patch_book_with_invalid_id(client: FlaskClient):

    request_data = {
        'title':'Harry Potter e a pedra filosofal'
    }   
    
    request_response = client.patch('/api/books/2fc09626-8a2c-4ef7-b59d-4a56e77e5719',json=request_data)

    assert (request_response.status_code == 404), 'Verificar se o status code é NOT FOUND'
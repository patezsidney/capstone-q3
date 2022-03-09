from flask.testing import FlaskClient


def test_edit_book_or_student_in_book_rental_by_id(client: FlaskClient):

    request_data = {
        "student_id":"2a465bd0-22cd-45e7-9fd1-142dee2cca78"
    }    
    
    request_response = client.patch("/api/library/23c3c4c8-d923-43d3-bc1b-c47d7b741ee1",json=request_data)
    
    assert (request_response.status_code == 202), "Verificar se o status code é ACCEPTED"

def test_edit_book_or_student_in_book_rental_by_id_with_incorrect_key(client: FlaskClient):

    request_data = {
        "student":"1d5225ef-5638-4397-9989-e604a2cceca0"
    }    
    
    request_response = client.patch("/api/library/3554e9f0-8208-4e99-81c1-d79f3caf891c",json=request_data)
    
    assert (request_response.status_code == 400), "Verificar se o status code é BAD REQUEST"

def test_edit_book_or_student_in_book_rental_by_id_with_incorrect_type_value(client: FlaskClient):

    request_data = {
        "student_id":1000000000000000000000000000000000
    }    
    
    request_response = client.patch("/api/library/51df51e0-00a7-49e3-9f2e-0405574f5c55",json=request_data)
    
    assert (request_response.status_code == 400), "Verificar se o status code é BAD REQUEST"

def test_edit_book_or_student_in_book_rental_by_id_with_invalid_id(client: FlaskClient):

    request_data = {
        "student_id":"1d5225ef-5638-4397-9989-e604a2cceca0"
    }    
    
    request_response = client.patch("/api/library/51df51e0-00a7-49e3-9f2e-0405574f5c55",json=request_data)
    
    assert (request_response.status_code == 404), "Verificar se o status code é NOT FOUND"
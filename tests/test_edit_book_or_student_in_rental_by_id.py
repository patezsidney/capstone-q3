from flask.testing import FlaskClient


def test_edit_book_or_student_in_book_rental_by_id(client: FlaskClient):

    request_data = {
        "student_id":"1d5225ef-5638-4397-9989-e604a2cceca0"
    }    
    
    request_response = client.patch("/api/library/023b926d-8f03-460d-be7b-840d80f91f6e",json=request_data)
    
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
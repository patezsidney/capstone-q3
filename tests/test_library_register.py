from flask.testing import FlaskClient


def test_register_rental(client: FlaskClient):

    request_data = {
        "employee_id":"3f5e5df3-651b-46ec-9c42-be4a863f974a",
        "book_id":"2fc09626-8a2c-4ef7-b59d-4a56e77e5714",
        "student_id":"51df51e0-00a7-49e3-9f2e-0405574f5c20"
    }    
    
    request_response = client.post("/api/library/rental",json=request_data)
    
    assert (request_response.status_code == 201), "Verificar se o status code é CREATED"

def test_rental_books_with_incorrect_key(client: FlaskClient):

    request_data = {
        "employee":"3f5e5df3-651b-46ec-9c42-be4a863f974a",
        "book_id":"2fc09626-8a2c-4ef7-b59d-4a56e77e5714",
        "student_id":"51df51e0-00a7-49e3-9f2e-0405574f5c20"
    }     
    
    request_response = client.post("/api/library/rental",json=request_data)
    
    assert (request_response.status_code == 400), "Verificar se o status code é BAD REQUEST"

def test_rental_books_with_incorrect_key_two(client: FlaskClient):

    request_data = {
        "book_id":"2fc09626-8a2c-4ef7-b59d-4a56e77e5714",
        "student_id":"51df51e0-00a7-49e3-9f2e-0405574f5c20"
    }     
    
    request_response = client.post("/api/library/rental",json=request_data)
    
    assert (request_response.status_code == 400), "Verificar se o status code é BAD REQUEST"
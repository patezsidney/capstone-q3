from flask.testing import FlaskClient


def test_register_book_rental_return_by_id(client: FlaskClient):

    request_data = {
        'employee_id':'b3298cfc-7fb8-47af-91ed-f2d8c4545cdd',
        'book_id' : '081c575b-a38f-4f41-bf15-2593cd58ab93', 
        'student_id' : '7dc82c28-4766-4bff-829b-2198a2e1ef98'
    }    
    
    request_response = client.patch("/api/library/return/201e6867-ec20-4834-b4ce-1f01b0b9e8db",json=request_data,headers={"Authorization": 'Bearer 1236'})
    
    assert (request_response.status_code == 202), "Verificar se o status code é ACCEPTED"

def test_register_book_rental_return_by_id_with_incorrect_key(client: FlaskClient):

    request_data = {
        'employee':'b3298cfc-7fb8-47af-91ed-f2d8c4545cdd',
        'book_id' : '081c575b-a38f-4f41-bf15-2593cd58ab93', 
        'student_id' : '7dc82c28-4766-4bff-829b-2198a2e1ef98'
    }    
    
    request_response = client.patch("/api/library/return/3554e9f0-8208-4e99-81c1-d79f3caf891c",json=request_data,headers={"Authorization": 'Bearer 1236'})
    
    assert (request_response.status_code == 400), "Verificar se o status code é BAD REQUEST"

def test_register_book_rental_return_by_id_with_incorrect_type_value(client: FlaskClient):

    request_data = {
        'employee_id': 0000000000000000000000000000000000000,
        'book_id' : '081c575b-a38f-4f41-bf15-2593cd58ab93', 
        'student_id' : '7dc82c28-4766-4bff-829b-2198a2e1ef98'
    }    
    
    request_response = client.patch("/api/library/return/51df51e0-00a7-49e3-9f2e-0405574f5c55",json=request_data,headers={"Authorization": 'Bearer 1236'})
    
    assert (request_response.status_code == 400), "Verificar se o status code é BAD REQUEST"

def test_edit_book_or_student_in_book_rental_by_id_with_invalid_id(client: FlaskClient):

    request_data = {
        'employee_id':'b3298cfc-7fb8-47af-91ed-f2d8c4545cdd',
        'book_id' : '081c575b-a38f-4f41-bf15-2593cd58ab93', 
        'student_id' : '7dc82c28-4766-4bff-829b-2198a2e1ef98'
    }    
    
    request_response = client.patch("/api/library/return/51df51e0-00a7-49e3-9f2e-0405574f5c55",json=request_data,headers={"Authorization": 'Bearer 1236'})
    
    assert (request_response.status_code == 404), "Verificar se o status code é NOT FOUND"
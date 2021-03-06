from flask.testing import FlaskClient
headers = {"Authorization": "Bearer 1234"}


def test_register_one_student(client: FlaskClient):

    request_data = {
        "name" : "Uzumake Naruto",
        "contact_name" : "Umino Iruka",
        "contact_email" : "IrukaTeacher@ninjaschool.com",
        "cpf" : "99999999999",
        "birth_date" : "1999/05/26",
        "gender" : "Masculino",
        "photo" : "alt.png",
        "password" : "viladafolhaoculta",
        "classroom_id" : "51df51e0-00a7-49e3-9f2e-0405574f5c20"       
    }    
    
    request_response = client.post("/api/students/register",json=request_data, headers=headers)
    assert (request_response.status_code == 201), "Verificar se o status code é OK"

def test_register_one_student_with_incorretc_key(client: FlaskClient):

    request_data = {
        "name" : "Uzumake Naruto",
        "contact" : "Umino Iruka", #nome da chave incorreto.
        "contact_email" : "IrukaTeacher@ninjaschool.com",
        "cpf" : "99999999999",
        "birth_date" : "1999/05/26",
        "gender" : "Masculino",
        "photo" : "",
        "password" : "viladafolhaoculta",
        "classroom_id" : "51df51e0-00a7-49e3-9f2e-0405574f5c20"        
    }    
    
    request_response = client.post("/api/students/register",json=request_data, headers=headers)
    
    assert (request_response.status_code == 400), "Verificar se o status code é BAD REQUEST"

def test_register_one_student_with_missing_key(client: FlaskClient):

    request_data = {
        "name" : "Uzumake Naruto",
        "contact_email" : "IrukaTeacher@ninjaschool.com",
        "cpf" : "99999999999",
        "birth_date" : "1999/05/26",
        "gender" : "Masculino",
        "photo" : "",
        "password" : "viladafolhaoculta",
        "classroom_id" : "51df51e0-00a7-49e3-9f2e-0405574f5c20"        
    }    
    
    request_response = client.post("/api/students/register",json=request_data, headers=headers)
    
    assert (request_response.status_code == 400), "Verificar se o status code é BAD REQUEST"

def test_register_one_student_with_incorretc_type_key(client: FlaskClient):

    request_data = {
        "name" : "Uzumake Naruto",
        "contact_name" : "Umino Iruka", 
        "contact_email" : "IrukaTeacher@ninjaschool.com",
        "cpf" : 00000000000,
        "birth_date" : "1999/05/26",
        "gender" : "Masculino",
        "photo" : "",
        "password" : "viladafolhaoculta",
        "classroom_id" : "51df51e0-00a7-49e3-9f2e-0405574f5c20"        
    }    
    
    request_response = client.post("/api/students/register",json=request_data, headers=headers)
    
    assert (request_response.status_code == 400), "Verificar se o status code é BAD REQUEST"

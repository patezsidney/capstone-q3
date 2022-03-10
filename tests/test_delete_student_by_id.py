from flask.testing import FlaskClient


def test_del_student_by_id(client: FlaskClient): 

    student_data = {
        "name" : "Uzumake Naruto",
        "contact_name" : "Umino Iruka",
        "contact_email" : "IrukaTeacher123@ninjaschool.com",
        "cpf" : "99999899999",
        "birth_date" : "1999/05/26",
        "gender" : "Masculino",
        "photo" : "alt.png",
        "password" : "viladafolhaoculta",
        "classroom_id" : "51df51e0-00a7-49e3-9f2e-0405574f5c20"       
    }    
    
    student_response = client.post("/api/students/register",json=student_data,headers={"Authorization": 'Bearer 1234'})
    student_json = student_response.get_json()
    request_response = client.delete(f"/api/students/{student_json['id']}",headers={"Authorization": 'Bearer 1234'})

      
    assert (request_response.status_code == 204), "Verificar se o status code é OK"

def test_del_student_with_ivld_key(client: FlaskClient):
    
    request_response = client.delete("/api/students/51df51e0-00a7-49e3-9f2e-0405574f5c88",headers={"Authorization": 'Bearer 1234'})
    
    assert (request_response.status_code == 404), "Verificar se o status code é NOT FOUND"
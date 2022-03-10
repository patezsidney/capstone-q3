from flask.testing import FlaskClient


def test_patch_edit_school_subject_by_id(client: FlaskClient):

    request_data = {
        "employee_id":"3f5e5df3-651b-46ec-9c42-be4a863f974a"
    }    
    
    request_response = client.patch("/api/school_subjects/edit/19c9807c-d818-4bc5-8d80-c66ad5ff253f",json=request_data)
    
    assert (request_response.status_code == 202), "Verificar se o status code é ACCEPTED"

def test_patch_edit_school_subject_by_id_two(client: FlaskClient):

    request_data = {
        "school_subject":"PHP"
    }    
    
    request_response = client.patch("/api/school_subjects/edit/62921285-ac00-4f38-ab44-356cdea16631",json=request_data)
    
    assert (request_response.status_code == 202), "Verificar se o status code é ACCEPTED"
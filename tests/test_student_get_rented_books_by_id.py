from flask.testing import FlaskClient


def test_student_get_rented_books_by_id(client: FlaskClient):

    response = client.get("/api/library/rented_books/1d5225ef-5638-4397-9989-e604a2cceca0")

    print("PRINT======>",response)

    response_json: list = response.get_json()

    print("PRINT======>",response_json)
    
    assert (type(response_json) is list), "Verificar se está retornando um lista"
    assert (len(response_json) == 1), "Verificar se está retornando 1 registro"
    assert (response.status_code == 200), "Verificar se o status code é OK"
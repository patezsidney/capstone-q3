def test_get_all_students(client):
    response = client.get("/students")

    assert (type(response.get_json()) is dict), "Verificar se está retornando um dict"


def test_status_rota_get_all_stundets(client):
    response = client.get("/students")

    assert response.status_code == 200, "Verificar se o status code é 200"
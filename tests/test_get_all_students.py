def test_status_rota_get_all_students(client):
    response = client.get("/api/students")

    assert response.status_code == 200, "Verificar se o status code é created"

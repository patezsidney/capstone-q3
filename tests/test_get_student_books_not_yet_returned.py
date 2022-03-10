def test_get_student_books_not_yet_returned(client):
    response = client.get("/api/library/rented/7dc82c28-4766-4bff-829b-2198a2e1ef98")

    assert response.status_code == 200, "Verificar se o status code é created"
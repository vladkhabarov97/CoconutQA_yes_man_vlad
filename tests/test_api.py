def test_api():
    response = {"status_code": 200}
    # Намеренная ошибка
    assert response["status_code"] == 999
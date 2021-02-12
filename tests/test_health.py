from app import main


def test_health(test_app):
    response = test_app.get("/health")
    assert response.status_code == 200
    assert response.json() == {"health": "OK", "environment": "dev", "testing": True}
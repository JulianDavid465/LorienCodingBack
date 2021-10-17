from fastapi.testclient import TestClient
from api import app

client = TestClient(app)


def test_create_game():
    response = client.post("/game/", json={"name": "partida1"})
    assert response.status_code == 201
    assert response.json() == {"id": 1, "name": "partida1"}


# Import TestClient to test FastAPI endpoints without running the server manually
from fastapi.testclient import TestClient

# Import the FastAPI app from main.py
from main import app


# Create a test client that can send requests to our API during testing
client = TestClient(app)


# Test the health check endpoint
# This verifies that the backend reports a healthy status
def test_health_check():
    response = client.get("/api/health")

    assert response.status_code == 200
    assert response.json()["status"] == "healthy"
    assert response.json()["service"] == "GTA 6 Companion App API"


# Test the player rank endpoint
# This verifies that the endpoint returns a list of player rank records
def test_player_rank():
    response = client.get("/api/player-rank")
    data = response.json()

    assert response.status_code == 200
    assert isinstance(data, list)
    assert len(data) >= 1
    assert data[0]["player_name"] == "Frantz"


# Test creating a new player rank entry
def test_create_player_rank():
    payload = {
        "player_name": "TestUser",
        "level": 5,
        "rank_title": "Beginner",
        "xp": 800,
        "xp_to_next_level": 200
    }

    response = client.post("/api/player-rank", json=payload)

    assert response.status_code == 200
    assert response.json()["player_name"] == "TestUser"
    assert response.json()["level"] == 5
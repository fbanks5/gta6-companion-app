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
# This verifies that player rank data returns correctly
def test_player_rank():
    response = client.get("/api/player-rank")
    data = response.json()

    assert response.status_code == 200
    assert data["player_name"] == "Frantz"
    assert data["level"] == 10
    assert data["rank_title"] == "Rising Hustler"
    assert data["xp"] == 2500
    assert data["xp_to_next_level"] == 500
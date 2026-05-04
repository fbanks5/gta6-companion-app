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
# This creates a player first, then verifies the endpoint returns a list of players.
def test_player_rank():
    payload = {
        "player_name": "ListTestPlayer",
        "level": 5,
        "rank_title": "List Tester",
        "xp": 400,
        "xp_to_next_level": 100
    }

    create_response = client.post("/api/player-rank", json=payload)
    assert create_response.status_code == 200

    response = client.get("/api/player-rank")
    data = response.json()

    assert response.status_code == 200
    assert isinstance(data, list)
    assert any(player["player_name"] == "ListTestPlayer" for player in data)



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


# Test retrieving a player by name
def test_get_player_by_name():
    payload = {
        "player_name": "Frantz",
        "level": 10,
        "rank_title": "Rising Hustler",
        "xp": 2500,
        "xp_to_next_level": 500
    }

    client.post("/api/player-rank", json=payload)

    response = client.get("/api/player-rank/Frantz")

    assert response.status_code == 200
    assert response.json()["player_name"]  == "Frantz"


# Test retrieving a non-existent player
def test_get_player_not_found():
    response = client.get("/api/player-rank/UnknownPlayer")

    assert response.status_code == 404


def test_delete_player_by_name():
    payload = {
        "player_name": "DeleteMe",
        "level": 10,
        "rank_title": "Temporary Player",
        "xp": 300,
        "xp_to_next_level": 100
    }

    create_response = client.post("/api/player-rank", json=payload)
    assert create_response.status_code == 200

    delete_response = client.delete("/api/player-rank/DeleteMe")
    assert delete_response.status_code == 200
    assert delete_response.json()["message"] == "Player 'DeleteMe' deleted successfully."

    lookup_response = client.get("api/player-rank/DeleteMe")
    assert lookup_response.status_code == 404


# Test deleting a player that does not exist
def test_delete_player_not_found():
    response = client.delete("/api/player-rank/NoSuchPlayer")

    assert response.status_code == 404



def test_update_player_by_name():
    payload = {
        "player_name": "UpdateMe",
        "level": 5,
        "rank_title": "Starter",
        "xp": 300,
        "xp_to_next_level": 100
    }

    client.post("/api/player-rank", json=payload)

    updated_payload = {
        "player_name": "UpdateMe",
        "level": 10,
        "rank_title": "Boss",
        "xp": 2000,
        "xp_to_next_level": 300
    }

    response = client.put("/api/player-rank/UpdateMe", json=updated_payload)

    assert response.status_code == 200
    assert response.json()["level"] == 10
    assert response.json()["rank_title"] == "Boss"



def test_update_player_not_found():
    payload = {
        "player_name": "Ghost",
        "level": 99,
        "rank_title": "Phantom",
        "xp": 9999,
        "xp_to_next_level": 0
    }

    response = client.put("/api/player-rank/Ghost", json=payload)

    assert response.status_code == 404


# Test that an empty player name is rejected
def test_create_player_with_empty_name_fails():
    payload = {
        "player_name": "",
        "level": 5,
        "rank_title": "Rookie",
        "xp": 500,
        "xp_to_next_level": 100
    }

    response = client.post("/api/player-rank", json=payload)

    assert response.status_code == 422


# Test that a negative level is rejected
def test_create_player_with_negative_level_fails():
    payload = {
        "player_name": "BadLevelPlayer",
        "level": -1,
        "rank_title": "Rookie",
        "xp": 500,
        "xp_to_next_level": 100
    }

    response = client.post("/api/player-rank", json=payload)

    assert response.status_code == 422



def test_create_player_with_negative_xp_fails():
    payload = {
        "player_name": "BadXpPlayer",
        "level": 5,
        "rank_title": "Rookie",
        "xp": -500,
        "xp_to_next_level": 100
    }

    response = client.post("/api/player-rank", json=payload)

    assert response.status_code == 422

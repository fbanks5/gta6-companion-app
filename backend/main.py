# Import FastAPI to create our API server
from fastapi import FastAPI

# Import BaseModel from Pydantic to define structured data models
from pydantic import BaseModel

# Create an instance of the FastAPI application
# This is the core of our backend API
app = FastAPI(
    title="GTA 6 Companion App API",
    description="Prototype API for tracking player rank",
    version="1.0.0"
)

# Define a data model for player rank information using Pydantic's BaseModel
# This ensures all responses follow a consistent structure
class PlayerRank(BaseModel):
    player_name: str
    level: int
    rank_title: str
    xp: int
    xp_to_next_level: int

# Root endpoint (basic health check)
# This lets us confirm the API is running
@app.get("/")
def home():
    return {"message": "Welcome to the GTA 6 Companion App API!"}

# Player rank endpoint
# This returns mock data for now (since we don't have real GTA data yet)
@app.get("/api/player-rank", response_model=PlayerRank)
def get_player_rank():
    return PlayerRank(
        player_name="Frantz",
        level=10,
        rank_title="Rising Hustler",
        xp=2500,
        xp_to_next_level=500
    )
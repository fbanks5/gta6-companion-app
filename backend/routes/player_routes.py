# Import APIRouter to organize related API endpoints
from fastapi import APIRouter

# Import the response model and service function
from models.player import PlayerRank
from services.player_service import get_mock_player_rank


# Create a router for player-related endpoints
router = APIRouter(
    prefix="/api",
    tags=["Player"]
)


# Player Rank endpoint
# This returns mock player rank data from the service layer
@router.get("/player-rank", response_model=PlayerRank)
def get_player_rank():
    return get_mock_player_rank()

@router.post("/player-rank", response_model=PlayerRank)
def create_player_rank(player: PlayerRank):
    """
    Accepts player data from the request body and returns it.
    For now, this simulates saving data (no database yet).
    """
    return player
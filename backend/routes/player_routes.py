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
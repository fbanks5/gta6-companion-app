from database import get_db
from sqlalchemy.orm import Session

# Import List so our GET endpoint can return multiple player rank records
from typing import List

# Import APIRouter to organize related API endpoints
from fastapi import APIRouter, HTTPException, Depends

# Import the response model and service functions
from models.player import PlayerRank
from services.player_service import(
    get_all_player_ranks,
    save_player_rank,
    get_player_by_name,
    delete_player_by_name,
    update_player_by_name
)


# Create a router for player-related endpoints
router = APIRouter(
    prefix="/api",
    tags=["Player"]
)


# Get all player rank records
# This returns every player rank currently stored in memory
@router.get("/player-rank", response_model=List[PlayerRank])
def get_player_rank(db: Session = Depends(get_db)):
    return get_all_player_ranks(db)



# Create a new player rank record
# This saves player-submitted rank data into temporary memory
@router.post("/player-rank", response_model=PlayerRank)
def create_player_rank(player: PlayerRank, db: Session = Depends(get_db)):
    """
    Accepts player data from the request body and returns it.
    For now, this simulates saving data (no database yet).
    """
    return save_player_rank(db, player)



# Get a specific player by name
# Returns player data or 404 if not found
@router.get("/player-rank/{player_name}", response_model=PlayerRank)
def get_player(player_name: str, db: Session = Depends(get_db)):
    player = get_player_by_name(db, player_name)

    if not player:
        raise HTTPException(status_code=404, detail="Player not found")

    return player

@router.delete("/player-rank/{player_name}")
def delete_player(player_name: str, db: Session = Depends(get_db)):
    deleted = delete_player_by_name(db, player_name)

    if not deleted:
        raise HTTPException(status_code=404, detail="Player not found")

    return {
        "message": f"Player '{player_name}' deleted successfully."
    }


# Update a specific player by name
@router.put("/player-rank/{player_name}", response_model=PlayerRank)
def update_player(
    player_name: str,
    updated_player: PlayerRank,
    db: Session = Depends(get_db)
):
    updated = update_player_by_name(db, player_name, updated_player)

    if updated is None:
        raise HTTPException(status_code=404, detail="Player not found")

    return updated


# Import BaseModel from Pydantic to define structured API data
from pydantic import BaseModel


# PlayerRank defines the structure of the player rank response
# This helps FastAPI validate and document the API response
class PlayerRank(BaseModel):
    player_name: str
    level: int
    rank_title: str
    xp: int
    xp_to_next_level: int
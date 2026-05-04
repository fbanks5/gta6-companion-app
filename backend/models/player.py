# Import BaseModel and Field from Pydantic
# BaseModel creates the schema, Field adds the validation rules
from pydantic import BaseModel, Field


# PlayerRank defines the shape and validation rules for player rank data
class PlayerRank(BaseModel):
    # Player name must be at least 1 character and no more than 50 characters
    player_name: str = Field(..., min_length=1, max_length=50)

    # Player level must be 1 or higher
    level: int = Field(..., ge=1)

    # Rank title must be at least 1 character and no more than 50 characters
    rank_title: str = Field(..., min_length=1, max_length=50)

    # XP cannot be negative
    xp: int = Field(..., ge=0)

    # XP needed for next level cannot be negative
    xp_to_next_level: int = Field(..., ge=0)
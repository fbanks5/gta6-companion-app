# Import List so we can store multiple PlayerRank objects in memory
from typing import List

# Import the player rank model so this service can return structured player data
from models.player import PlayerRank


# Temporary in-memory storage for player ranks
# This acts like a fake database while we build the prototype
player_rank_storage: List[PlayerRank] = [
    PlayerRank(
        player_name="Frantz",
        level=10,
        rank_title="Rising Hustler",
        xp=2500,
        xp_to_next_level=500
    )
]

# Return all saved player rank records
def get_all_player_ranks() -> List[PlayerRank]:
    return player_rank_storage


# Save a new player rank record into memory
def save_player_rank(player: PlayerRank) -> PlayerRank:
    player_rank_storage.append(player)
    return player


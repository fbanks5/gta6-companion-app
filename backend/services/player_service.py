# Import List so we can store multiple PlayerRank objects in memory
from typing import List, Optional

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


def get_player_by_name(name: str):
    for player in player_rank_storage:
        if player.player_name.lower() == name.lower():
            return player
    return None

# Delete a player by name using a case-insensitive search.
# Returns True if a player was deleted, or False if no matching player exists.
def delete_player_by_name(player_name: str):
    for index, player in enumerate(player_rank_storage):
        if player.player_name.lower() == player_name.lower():
            del player_rank_storage[index]
            return True

    return False


# Update an existing player by name.
# Returns the updated player if found, otherwise None.
def update_player_by_name(player_name: str, updated_player: PlayerRank) -> Optional[PlayerRank]:
    for index, player in enumerate(player_rank_storage):
        if player.player_name.lower() == player_name.lower():
            player_rank_storage[index] = updated_player
            return updated_player

    return None





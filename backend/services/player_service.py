# Import the player rank model so this service can return structured player data
from models.player import PlayerRank


# This function return the mock player rank data for the prototype
# Later, this can be replaced with the database logic or real integrations
def get_mock_player_rank() -> PlayerRank:
    return PlayerRank(
        player_name="Frantz",
        level=10,
        rank_title="Rising Hustler",
        xp=2500,
        xp_to_next_level=500
    )



from sqlalchemy.orm import Session
from db_models import PlayerRankDB
from models.player import PlayerRank

# Import List so we can store multiple PlayerRank objects in memory
from typing import List, Optional

# Import the player rank model so this service can return structured player data
from models.player import PlayerRank


# Get all players
def get_all_player_ranks(db: Session):
    players = db.query(PlayerRankDB).all()

    return [
        PlayerRank(
            player_name=p.player_name,
            level=p.level,
            rank_title=p.rank_title,
            xp=p.xp,
            xp_to_next_level=p.xp_to_next_level
        )
        for p in players
    ]


# Save new player
def save_player_rank(db: Session, player: PlayerRank):
    db_player = PlayerRankDB(
        player_name=player.player_name,
        level=player.level,
        rank_title=player.rank_title,
        xp=player.xp,
        xp_to_next_level=player.xp_to_next_level
    )

    db.add(db_player)
    db.commit()
    db.refresh(db_player)

    return player


# Get player by name
def get_player_by_name(db: Session, name: str):
    player = db.query(PlayerRankDB).filter(
        PlayerRankDB.player_name.ilike(name)
    ).first()

    if not player:
        return None

    return PlayerRank(
        player_name=player.player_name,
        level=player.level,
        rank_title=player.rank_title,
        xp=player.xp,
        xp_to_next_level=player.xp_to_next_level
    )


# Delete player
def delete_player_by_name(db: Session, player_name: str):
    player = db.query(PlayerRankDB).filter(
        PlayerRankDB.player_name.ilike(player_name)
    ).first()

    if not player:
        return False

    db.delete(player)
    db.commit()
    return True


# Update player
def update_player_by_name(db: Session, player_name: str, updated_player: PlayerRank):
    player = db.query(PlayerRankDB).filter(
        PlayerRankDB.player_name.ilike(player_name)
    ).first()

    if not player:
        return None

    player.level = updated_player.level
    player.rank_title = updated_player.rank_title
    player.xp = updated_player.xp
    player.xp_to_next_level = updated_player.xp_to_next_level

    db.commit()
    db.refresh(player)

    return updated_player






from sqlalchemy.orm import Session
from db_models import PlayerRankDB

def seed_players(db: Session):
    existing = db.query(PlayerRankDB).first()

    # Prevent duplicate seeding
    if existing:
        return

    sample_players = [
        PlayerRankDB(
            player_name="Frantz",
            level=25,
            rank_title="Street Legend",
            xp=12000,
            xp_to_next_level=3000
        ),
        PlayerRankDB(
            player_name="PlayerOne",
            level=10,
            rank_title="Rising Hustler",
            xp=2500,
            xp_to_next_level=500
        )
    ]

    db.add_all(sample_players)
    db.commit()
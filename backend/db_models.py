# Import SQLAlchemy column types
from sqlalchemy import Column, Integer, String

# Import Base so this model can become a real database table
from database import Base


# PlayerRankDB represents the player_ranks table in SQLite
class PlayerRankDB(Base):
    __tablename__ = "player_ranks"

    id = Column(Integer, primary_key=True, index=True)
    player_name = Column(String, unique=True, index=True, nullable=False)
    level = Column(Integer, nullable=False)
    rank_title = Column(String, nullable=False)
    xp = Column(Integer, nullable=False)
    xp_to_next_level = Column(Integer, nullable=False)
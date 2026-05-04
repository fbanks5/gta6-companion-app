# Import SQLAlchemy tools for creating the database engine and sessions
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


# SQLite database file location
# This creates a local file named gta6_companion.db inside the backend folder
DATABASE_URL = "sqlite:///./gta6_companion.db"


# Create the SQLite engine
# check_same_thread=False is needed so FastAPI can use SQLite safely during requests
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)


# Create database sessions
# Each session is used to talk to the database
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


# Base class used by SQLAlchemy models
Base = declarative_base()

# Dependency-style helper for getting a database session
def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()
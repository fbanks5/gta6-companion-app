# Import pytest to create reusable test setup fixtures
import pytest

# Import SQLAlchemy tools for creating a separate test database
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Import FastAPI app and database dependencies
from main import app
from database import Base, get_db
from rate_limiter import limiter

# Disable rate limiting during tests
# All pytest requests come from the same testclient",
# so without this, tests will hit the limit and fail randomly
limiter.enabled = False

# Test database file
# This keeps tests separate from your real development database
TEST_DATABASE_URL = "sqlite:///./test_gta6_companion.db"

# Create a separate SQLite engine for testing
test_engine = create_engine(
    TEST_DATABASE_URL,
    connect_args={"check_same_thread": False}
)

# Create test database sessions
TestingSessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=test_engine
)

# Override the normal app database dependency
# During tests, FastAPI will use the test database instead of gta6_companion_db
def override_get_db():
    db = TestingSessionLocal()

    try:
        yield db
    finally:
        db.close()


# Apply the database override to the FastAPI app
app.dependency_overrides[get_db] = override_get_db


# Reset the test database before every test
# This keeps each test independent and prevents duplicate player_name conflicts
@pytest.fixture(autouse=True)
def reset_test_database():
    Base.metadata.drop_all(bind=test_engine)
    Base.metadata.create_all(bind=test_engine)

    yield

    Base.metadata.drop_all(bind=test_engine)
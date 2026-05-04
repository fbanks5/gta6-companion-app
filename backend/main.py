
from seed_data import seed_players
from database import SessionLocal
from database import engine
from db_models import Base

# Import FastAPI to create our API server
from fastapi import FastAPI

# Import the player routes so they can be registered with the app
from routes.player_routes import router as player_router

# Import health routes so they can be registered with the app
from routes.health_routes import router as health_router

# Create an instance of the FastAPI application
# This is the core of our backend API
app = FastAPI(
    title="GTA 6 Companion App API",
    description="Prototype API for tracking player rank and future AI insights.",
    version="0.1.0"
)

# Create database tables automatically on startup
Base.metadata.create_all(bind=engine)


@app.on_event("startup")
def startup():
    db = SessionLocal()
    try:
        seed_players(db)
    finally:
        db.close()

# Root endpoint (basic health check)
# This lets us confirm the API is running
@app.get("/")
def home():
    return {"message": "Welcome to the GTA 6 Companion App API!"}

# Register player-related routes with the main app
app.include_router(player_router)

# Register health-check routes with the main app
app.include_router(health_router)
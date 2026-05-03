# Import FastAPI to create our API server
from fastapi import FastAPI

# Import the player routes so they can be registered with the app
from routes.player_routes import router as player_router

# Create an instance of the FastAPI application
# This is the core of our backend API
app = FastAPI(
    title="GTA 6 Companion App API",
    description="Prototype API for tracking player rank and future AI insights.",
    version="1.0.0"
)


# Root endpoint (basic health check)
# This lets us confirm the API is running
@app.get("/")
def home():
    return {"message": "Welcome to the GTA 6 Companion App API!"}

# Register player-related routes with the main app
app.include_router(player_router)
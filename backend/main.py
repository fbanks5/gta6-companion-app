from rate_limiter import limiter
from slowapi.errors import RateLimitExceeded
from slowapi.middleware import SlowAPIMiddleware
from fastapi import Request
from fastapi.responses import JSONResponse
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

from fastapi.middleware.cors import CORSMiddleware

# =========================
# SECURITY HEADERS MIDDLEWARE
# =========================

@app.middleware("http")
async def add_security_headers(request, call_next):
    response = await call_next(request)

    # Prevent MIMI-type sniffing
    response.headers["X-Content-Type-Options"] = "nosniff"

    # Prevent clickjacking attacks
    response.headers["X-Frame-Options"] = "DENY"

    # Basic XSS protection (legacy but still useful)
    response.headers["X-XSS-Protection"] = "1; mode=block"

    # Enforce HTTPS (important in production)
    response.headers["Strict-Transport-Security"] = "max-age=31536000; includeSubDomains"

    return response



# Store the limited on the FastAPI app so routes can use it
app.state.limiter = limiter

# Add SlowAPI middleware so rate limits are enforced during requests
app.add_middleware(SlowAPIMiddleware)


# Custom handler for rate limit violations
# This returns a clean JSON response instead of a default server error.
@app.exception_handler(RateLimitExceeded)
def rate_limit_handler(request: Request, exc: RateLimitExceeded):
    return JSONResponse(
        status_code=429,
        content={
            "detail": "Rate limit exceeded.  Please try again later."
        }
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
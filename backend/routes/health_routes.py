# Import APIRouter to organize health-related API endpoints
from fastapi import APIRouter

# Create a router for health-check endpoints
router = APIRouter(
    prefix="/api",
    tags=["Health"]
)

# Health check endpoint
# This confirms the backend service is running and ready to receive requests
@router.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "GTA 6 Companion App API",
        "version": "0.1.0"
    }
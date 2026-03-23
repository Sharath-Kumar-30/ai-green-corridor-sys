from fastapi import APIRouter

router = APIRouter()

# Include your endpoint routes here
from .endpoints import users, ambulance, traffic, hospital

router.include_router(users.router, prefix="/users", tags=["users"])
router.include_router(ambulance.router, prefix="/ambulance", tags=["ambulance"])
router.include_router(traffic.router, prefix="/traffic", tags=["traffic"])
router.include_router(hospital.router, prefix="/hospital", tags=["hospital"])
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Optional

router = APIRouter()

class AmbulanceRequest(BaseModel):
    user_id: int
    location: str
    images: Optional[List[str]] = None
    documents: Optional[List[str]] = None

class AmbulanceResponse(BaseModel):
    request_id: int
    status: str
    message: str

@router.post("/request-ambulance", response_model=AmbulanceResponse)
async def request_ambulance(request: AmbulanceRequest):
    # Here you would typically save the request to the database and notify the ambulance service
    # For demo purposes, we will return a mock response
    return AmbulanceResponse(request_id=1, status="success", message="Ambulance requested successfully.")

@router.get("/ambulance-status/{request_id}", response_model=AmbulanceResponse)
async def get_ambulance_status(request_id: int):
    # Here you would typically fetch the status from the database
    # For demo purposes, we will return a mock response
    return AmbulanceResponse(request_id=request_id, status="on the way", message="Ambulance is on the way to your location.")
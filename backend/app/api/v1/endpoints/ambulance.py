from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

router = APIRouter()

class AmbulanceRequest(BaseModel):
    request_id: str
    location: str
    user_id: str
    status: str

class Notification(BaseModel):
    request_id: str
    message: str

# Mock data
ambulance_requests = [
    {"request_id": "1", "location": "123 Main St", "user_id": "1", "status": "pending"}
]
notifications = []

@router.post("/request", response_model=AmbulanceRequest)
async def request_ambulance(request: AmbulanceRequest):
    ambulance_requests.append(request.dict())
    return request

@router.get("/notifications", response_model=List[AmbulanceRequest])
async def get_notifications():
    return ambulance_requests

@router.post("/notify", response_model=Notification)
async def notify_ambulance(notification: Notification):
    notifications.append(notification.dict())
    return notification

@router.get("/status/{request_id}", response_model=AmbulanceRequest)
async def get_request_status(request_id: str):
    for request in ambulance_requests:
        if request["request_id"] == request_id:
            return AmbulanceRequest(**request)
    raise HTTPException(status_code=404, detail="Request not found")
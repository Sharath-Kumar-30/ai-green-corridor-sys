from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

router = APIRouter()

class TrafficControlRequest(BaseModel):
    video_file: str
    ambulance_request_id: str

class TrafficControlResponse(BaseModel):
    status: str
    message: str
    green_signal: bool

# Mock data
traffic_updates = []

@router.post("/traffic-control", response_model=TrafficControlResponse)
async def traffic_control(request: TrafficControlRequest):
    if request.video_file and request.ambulance_request_id:
        detected = True
        traffic_updates.append({
            "ambulance_request_id": request.ambulance_request_id,
            "detected": detected,
            "green_signal": True
        })
        return TrafficControlResponse(
            status="success",
            message="Ambulance detected, green signal given.",
            green_signal=True
        )
    else:
        raise HTTPException(status_code=400, detail="Invalid request data")

@router.get("/status", response_model=List[dict])
async def get_traffic_updates():
    return traffic_updates
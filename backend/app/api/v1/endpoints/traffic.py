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

@router.post("/traffic-control", response_model=TrafficControlResponse)
async def traffic_control(request: TrafficControlRequest):
    # Simulate video detection logic
    if request.video_file and request.ambulance_request_id:
        # Here you would normally call the YOLO model for detection
        # For demo purposes, we will fake the detection
        detected = True  # Simulating detection of ambulance

        if detected:
            return TrafficControlResponse(
                status="success",
                message="Ambulance detected, green signal given.",
                green_signal=True
            )
        else:
            return TrafficControlResponse(
                status="failure",
                message="No ambulance detected.",
                green_signal=False
            )
    else:
        raise HTTPException(status_code=400, detail="Invalid request data")
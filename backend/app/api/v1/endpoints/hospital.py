from fastapi import APIRouter, HTTPException
from typing import List
from pydantic import BaseModel

router = APIRouter()

class PatientData(BaseModel):
    request_id: str
    symptoms: str
    location: str
    documents: List[str] = []

class HospitalNotification(BaseModel):
    request_id: str
    status: str
    message: str

# Mock data
hospital_notifications = [
    {"request_id": "1", "status": "pending", "message": "Patient incoming"}
]

@router.post("/notify", response_model=HospitalNotification)
async def notify_hospital(patient_data: PatientData):
    hospital_notifications.append({
        "request_id": patient_data.request_id,
        "status": "success",
        "message": "Hospital notified successfully."
    })
    return HospitalNotification(
        request_id=patient_data.request_id,
        status="success",
        message="Hospital notified successfully."
    )

@router.get("/status/{request_id}", response_model=HospitalNotification)
async def get_status(request_id: str):
    return HospitalNotification(
        request_id=request_id,
        status="pending",
        message="Waiting for hospital response."
    )

@router.get("/notifications", response_model=List[HospitalNotification])
async def get_notifications():
    return [HospitalNotification(request_id=n["request_id"], status=n["status"], message=n["message"]) for n in hospital_notifications]
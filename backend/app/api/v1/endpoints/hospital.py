from fastapi import APIRouter, HTTPException
from typing import List
from pydantic import BaseModel

router = APIRouter()

class PatientData(BaseModel):
    request_id: str
    symptoms: str
    location: str
    documents: List[str]  # List of document URLs

class HospitalNotification(BaseModel):
    request_id: str
    status: str
    message: str

@router.post("/notify", response_model=HospitalNotification)
async def notify_hospital(patient_data: PatientData):
    # Here you would typically send a notification to the hospital
    # For demo purposes, we will just return a success message
    return HospitalNotification(
        request_id=patient_data.request_id,
        status="success",
        message="Hospital notified successfully."
    )

@router.get("/status/{request_id}", response_model=HospitalNotification)
async def get_status(request_id: str):
    # Here you would typically check the status of the request
    # For demo purposes, we will return a dummy status
    return HospitalNotification(
        request_id=request_id,
        status="pending",
        message="Waiting for hospital response."
    )
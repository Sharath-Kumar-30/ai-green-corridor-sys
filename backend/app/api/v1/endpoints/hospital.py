from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text
from typing import List
from pydantic import BaseModel
from app.db.session import get_db

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

@router.post("/notify", response_model=HospitalNotification)
async def notify_hospital(patient_data: PatientData, db: Session = Depends(get_db)):
    try:
        query = text("""
            INSERT INTO hospital_notifications (ambulance_request_id, patient_symptoms, notification_time)
            VALUES (:request_id, :symptoms, NOW())
        """)
        db.execute(query, {
            "request_id": int(patient_data.request_id),
            "symptoms": patient_data.symptoms
        })
        db.commit()
        return HospitalNotification(
            request_id=patient_data.request_id,
            status="success",
            message="Hospital notified successfully."
        )
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/status/{request_id}", response_model=HospitalNotification)
async def get_status(request_id: str, db: Session = Depends(get_db)):
    try:
        query = text("SELECT patient_symptoms FROM hospital_notifications WHERE ambulance_request_id = :request_id ORDER BY notification_time DESC LIMIT 1")
        result = db.execute(query, {"request_id": int(request_id)})
        row = result.fetchone()
        status = "pending"
        message = "Waiting for hospital response."
        if row:
            status = "notified"
            message = f"Symptoms: {row[0]}"
        return HospitalNotification(request_id=request_id, status=status, message=message)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/notifications", response_model=List[dict])
async def get_notifications(db: Session = Depends(get_db)):
    try:
        query = text("""
            SELECT hn.ambulance_request_id, hn.patient_symptoms, hn.notification_time, ar.location
            FROM hospital_notifications hn
            LEFT JOIN ambulance_requests ar ON hn.ambulance_request_id = ar.id
            ORDER BY hn.notification_time DESC LIMIT 10
        """)
        result = db.execute(query)
        rows = result.fetchall()
        return [
            {
                "request_id": row[0],
                "symptoms": row[1],
                "location": row[3],
                "notification_time": str(row[2])
            } for row in rows
        ]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
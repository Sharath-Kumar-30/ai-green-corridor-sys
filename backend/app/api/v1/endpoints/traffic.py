from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text
from pydantic import BaseModel
from typing import List
from app.db.session import get_db

router = APIRouter()

class TrafficControlRequest(BaseModel):
    video_file: str
    ambulance_request_id: str

class TrafficControlResponse(BaseModel):
    status: str
    message: str
    green_signal: bool

@router.post("/traffic-control", response_model=TrafficControlResponse)
async def traffic_control(request: TrafficControlRequest, db: Session = Depends(get_db)):
    try:
        if request.video_file and request.ambulance_request_id:
            # Insert traffic notification
            query = text("""
                INSERT INTO traffic_notifications (ambulance_request_id, status, notification_time)
                VALUES (:request_id, 'green_signal', NOW())
            """)
            db.execute(query, {"request_id": int(request.ambulance_request_id)})
            db.commit()
            
            return TrafficControlResponse(
                status="success",
                message="Ambulance detected, green signal given.",
                green_signal=True
            )
        else:
            raise HTTPException(status_code=400, detail="Invalid request data")
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/status", response_model=List[dict])
async def get_traffic_updates(db: Session = Depends(get_db)):
    try:
        query = text("""
            SELECT tn.ambulance_request_id, tn.status, tn.notification_time, ar.location
            FROM traffic_notifications tn
            LEFT JOIN ambulance_requests ar ON tn.ambulance_request_id = ar.id
            ORDER BY tn.notification_time DESC LIMIT 10
        """)
        result = db.execute(query)
        rows = result.fetchall()
        return [
            {
                "ambulance_request_id": row[0],
                "status": row[1],
                "location": row[3],
                "notification_time": str(row[2])
            } for row in rows
        ]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text
from pydantic import BaseModel
from typing import List
from app.db.session import get_db

router = APIRouter()

class AmbulanceRequest(BaseModel):
    request_id: str
    location: str
    user_id: str
    status: str

class Notification(BaseModel):
    request_id: str
    message: str

@router.post("/request", response_model=AmbulanceRequest)
async def request_ambulance(request: AmbulanceRequest, db: Session = Depends(get_db)):
    try:
        query = text("""
            INSERT INTO ambulance_requests (user_id, location, status, request_time)
            VALUES (:user_id, :location, :status, NOW())
            RETURNING id
        """)
        result = db.execute(query, {
            "user_id": int(request.user_id),
            "location": request.location,
            "status": request.status
        })
        db.commit()
        row = result.fetchone()
        return AmbulanceRequest(
            request_id=str(row[0]),
            location=request.location,
            user_id=request.user_id,
            status=request.status
        )
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/notifications", response_model=List[dict])
async def get_notifications(db: Session = Depends(get_db)):
    try:
        query = text("SELECT id, location, status, request_time FROM ambulance_requests ORDER BY request_time DESC LIMIT 10")
        result = db.execute(query)
        rows = result.fetchall()
        return [{"id": row[0], "location": row[1], "status": row[2], "request_time": str(row[3])} for row in rows]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/notify", response_model=Notification)
async def notify_ambulance(notification: Notification, db: Session = Depends(get_db)):
    try:
        query = text("""
            UPDATE ambulance_requests SET status = 'acknowledged'
            WHERE id = :request_id
        """)
        db.execute(query, {"request_id": int(notification.request_id)})
        db.commit()
        return notification
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/status/{request_id}", response_model=AmbulanceRequest)
async def get_request_status(request_id: str, db: Session = Depends(get_db)):
    try:
        query = text("SELECT id, location, user_id, status FROM ambulance_requests WHERE id = :request_id")
        result = db.execute(query, {"request_id": int(request_id)})
        row = result.fetchone()
        if not row:
            raise HTTPException(status_code=404, detail="Request not found")
        return AmbulanceRequest(request_id=str(row[0]), location=row[1], user_id=str(row[2]), status=row[3])
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
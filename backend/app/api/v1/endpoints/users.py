from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text
from pydantic import BaseModel
from typing import List, Optional
from app.db.session import get_db

router = APIRouter()

class AmbulanceRequest(BaseModel):
    location: str
    user_id: int = 1

class AmbulanceResponse(BaseModel):
    request_id: int
    status: str
    message: str

@router.post("/request-ambulance", response_model=AmbulanceResponse)
async def request_ambulance(request: AmbulanceRequest, db: Session = Depends(get_db)):
    try:
        query = text("""
            INSERT INTO ambulance_requests (user_id, location, status, request_time)
            VALUES (:user_id, :location, 'pending', NOW())
            RETURNING id, status
        """)
        result = db.execute(query, {"user_id": request.user_id, "location": request.location})
        db.commit()
        row = result.fetchone()
        return AmbulanceResponse(
            request_id=row[0],
            status=row[1],
            message="Ambulance requested successfully."
        )
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/ambulance-status/{request_id}", response_model=AmbulanceResponse)
async def get_ambulance_status(request_id: int, db: Session = Depends(get_db)):
    try:
        query = text("SELECT id, status FROM ambulance_requests WHERE id = :request_id")
        result = db.execute(query, {"request_id": request_id})
        row = result.fetchone()
        if not row:
            raise HTTPException(status_code=404, detail="Request not found")
        return AmbulanceResponse(
            request_id=row[0],
            status=row[1],
            message=f"Status: {row[1]}"
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
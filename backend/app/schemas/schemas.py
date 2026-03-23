from pydantic import BaseModel
from typing import List, Optional

class UserRequest(BaseModel):
    user_id: str
    location: str
    images: List[str] = []
    documents: List[str] = []

class AmbulanceResponse(BaseModel):
    request_id: str
    status: str
    estimated_time: Optional[str] = None

class TrafficControlNotification(BaseModel):
    request_id: str
    traffic_signal: str
    message: str

class HospitalNotification(BaseModel):
    request_id: str
    patient_symptoms: str
    patient_id: str

class VideoUpload(BaseModel):
    request_id: str
    video_url: str
    video_type: str  # e.g., 'ambulance' or 'normal'
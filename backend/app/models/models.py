from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from backend.app.db.base import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    phone_number = Column(String, unique=True, index=True)
    location = Column(String)
    ambulance_requests = relationship("AmbulanceRequest", back_populates="user")

class AmbulanceRequest(Base):
    __tablename__ = "ambulance_requests"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    status = Column(String, default="pending")
    location = Column(String)
    timestamp = Column(String)

    user = relationship("User", back_populates="ambulance_requests")

class TrafficControl(Base):
    __tablename__ = "traffic_controls"

    id = Column(Integer, primary_key=True, index=True)
    request_id = Column(Integer, ForeignKey("ambulance_requests.id"))
    signal_status = Column(String, default="red")
    timestamp = Column(String)

    ambulance_request = relationship("AmbulanceRequest")

class Hospital(Base):
    __tablename__ = "hospitals"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    location = Column(String)
    notifications = relationship("HospitalNotification", back_populates="hospital")

class HospitalNotification(Base):
    __tablename__ = "hospital_notifications"

    id = Column(Integer, primary_key=True, index=True)
    hospital_id = Column(Integer, ForeignKey("hospitals.id"))
    patient_info = Column(String)
    timestamp = Column(String)

    hospital = relationship("Hospital", back_populates="notifications")
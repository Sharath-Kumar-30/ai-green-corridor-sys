from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1.endpoints import users, ambulance, traffic, hospital
from app.core.config import settings

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this as needed for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users.router, prefix="/api/v1/users", tags=["users"])
app.include_router(ambulance.router, prefix="/api/v1/ambulance", tags=["ambulance"])
app.include_router(traffic.router, prefix="/api/v1/traffic", tags=["traffic"])
app.include_router(hospital.router, prefix="/api/v1/hospital", tags=["hospital"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the AI-based Green Corridor System for Ambulances!"}
CREATE EXTENSION IF NOT EXISTS postgis;

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    phone VARCHAR(15) NOT NULL,
    location GEOGRAPHY(POINT, 4326),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE ambulance_requests (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id),
    status VARCHAR(50) NOT NULL,
    request_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    response_time TIMESTAMP,
    location GEOGRAPHY(POINT, 4326)
);

CREATE TABLE traffic_notifications (
    id SERIAL PRIMARY KEY,
    ambulance_request_id INT REFERENCES ambulance_requests(id),
    status VARCHAR(50) NOT NULL,
    notification_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE hospital_notifications (
    id SERIAL PRIMARY KEY,
    ambulance_request_id INT REFERENCES ambulance_requests(id),
    patient_symptoms TEXT,
    notification_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE video_uploads (
    id SERIAL PRIMARY KEY,
    ambulance_request_id INT REFERENCES ambulance_requests(id),
    video_url TEXT NOT NULL,
    upload_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
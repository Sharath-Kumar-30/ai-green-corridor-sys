-- Create the contents of the file: /ai-green-corridor-sys/ai-green-corridor-sys/backend/app/db/init_db.sql --

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    phone VARCHAR(15) NOT NULL,
    location GEOGRAPHY(Point, 4326),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE ambulance_requests (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id),
    status VARCHAR(50) NOT NULL,
    request_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    location GEOGRAPHY(Point, 4326)
);

CREATE TABLE ambulance_notifications (
    id SERIAL PRIMARY KEY,
    request_id INTEGER REFERENCES ambulance_requests(id),
    response_team_id INTEGER,
    acknowledged BOOLEAN DEFAULT FALSE,
    notification_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE traffic_control_notifications (
    id SERIAL PRIMARY KEY,
    request_id INTEGER REFERENCES ambulance_requests(id),
    signal_status VARCHAR(50) NOT NULL,
    notification_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE hospitals (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    location GEOGRAPHY(Point, 4326),
    contact_info VARCHAR(100)
);

CREATE TABLE hospital_notifications (
    id SERIAL PRIMARY KEY,
    hospital_id INTEGER REFERENCES hospitals(id),
    request_id INTEGER REFERENCES ambulance_requests(id),
    patient_symptoms TEXT,
    notification_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
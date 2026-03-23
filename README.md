# AI Green Corridor - Demo (Short Instructions)

Prerequisites (Windows with WSL2)
- Docker Desktop (WSL2 integration enabled)
- At least 4GB free RAM for containers

Quick run
1. Open WSL2 shell and cd to project root:

```bash
cd /path/to/ai-green-corridor-sys
```

2. Build and start services:

```bash
docker compose up --build -d
```

3. Watch backend logs during startup:

```bash
docker compose logs -f backend
```

4. After services are up, open the frontend at http://localhost:4200 and backend docs at http://localhost:8000/docs

Stopping and cleanup:

```bash
docker compose down -v
```

Demo tips
- Create a new request, upload a file named with 'ambulance' to force detection, observe status change.
# AI Based Green Corridor System for Ambulances

## Project Overview
The AI Based Green Corridor System for Ambulances is an MVP (Minimum Viable Product) designed to enhance emergency healthcare services using AI technology. The system facilitates real-time communication between users, ambulance response teams, traffic control, and hospitals to ensure timely medical assistance.

## Features
1. **User Screen**: 
   - Users can request an ambulance.
   - Share their location and upload pictures or PDFs.

2. **Ambulance/Emergency Response Teams Screen**: 
   - Receive notifications for ambulance requests.
   - Acknowledge requests and send notifications back to users and traffic control teams.

3. **Traffic Control Screen**: 
   - Get notified of ambulance requests and vague paths.
   - Simulate video detection using a YOLO model to manage traffic signals along the route.

4. **Hospital Screen**: 
   - Receive notifications about incoming patients and their symptoms.
   - Access uploaded documents (PDFs, images) for preparation.

## Tech Stack
- **Backend**:
  - Python 3.14.2
  - FastAPI
  - SQLAlchemy (ORM)
  - Alembic (Migrations)
  - Celery (Task Queue)
  - RabbitMQ (Message Broker)
  - PostgreSQL (Database)
  - MinIO (Object Storage)

- **Frontend**:
  - Angular
  - TypeScript
  - HTML/CSS

- **Infrastructure**:
  - Docker
  - Docker Compose
  - Nginx (Reverse Proxy)

## Architecture
The architecture consists of multiple services that communicate with each other:
- **Frontend**: Angular application serving the user interface.
- **Backend**: FastAPI application handling business logic and API endpoints.
- **Database**: PostgreSQL for data storage.
- **Message Broker**: RabbitMQ for handling asynchronous communication.
- **Object Storage**: MinIO for storing uploaded files.
- **Task Queue**: Celery for background processing tasks.

## Endpoints
- **User Endpoints**:
  - `POST /api/v1/users/request-ambulance`: Request an ambulance.
  - `POST /api/v1/users/upload`: Upload files (pictures, PDFs).

- **Ambulance Endpoints**:
  - `GET /api/v1/ambulance/notifications`: Get notifications for ambulance requests.

- **Traffic Control Endpoints**:
  - `GET /api/v1/traffic/notifications`: Get traffic control notifications.

- **Hospital Endpoints**:
  - `GET /api/v1/hospital/notifications`: Get notifications about incoming patients.

## How to Run the Project
1. **Clone the Repository**:
   ```
   git clone <repository-url>
   cd ai-green-corridor-sys
   ```

2. **Build and Run with Docker Compose**:
   ```
   docker-compose up --build
   ```

3. **Access the Application**:
   - Frontend: `http://localhost:4200`
   - Backend: `http://localhost:8000`

## Demo Instructions
1. **User Requests an Ambulance**: 
   - Navigate to the user screen and fill out the request form.
   - Upload any necessary documents.

2. **Ambulance Response**: 
   - Switch to the ambulance response team screen to see the incoming request.
   - Acknowledge the request and send a notification back.

3. **Traffic Control Simulation**: 
   - Go to the traffic control screen to simulate video detection.
   - Upload videos and observe the traffic signal changes based on the detection.

4. **Hospital Preparation**: 
   - Access the hospital screen to view incoming patient notifications and prepare accordingly.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.
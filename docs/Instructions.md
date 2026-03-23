# Instructions for Setting Up and Running the AI-Based Green Corridor System for Ambulances

## Prerequisites

1. **Docker Desktop**: Ensure that Docker Desktop is installed and running on your Windows machine.
2. **Git**: Install Git to clone the repository.
3. **Node.js**: Install Node.js to run the Angular frontend.

## Project Structure

The project is structured as follows:

```
ai-green-corridor-sys
├── backend
├── frontend
├── infra
├── services
├── scripts
├── docs
├── .gitignore
├── README.md
└── LICENSE
```

## Setup Instructions

1. **Clone the Repository**:
   Open a terminal and run the following command to clone the project repository:
   ```
   git clone <repository-url>
   cd ai-green-corridor-sys
   ```

2. **Build and Run the Docker Containers**:
   Navigate to the `infra` directory and run the following command to build and start all services:
   ```
   docker-compose up --build
   ```

3. **Access the Services**:
   - **Frontend**: Open your web browser and go to `http://localhost:4200` to access the Angular frontend.
   - **Backend**: The FastAPI backend will be accessible at `http://localhost:8000`.

4. **Database Initialization**:
   The PostgreSQL database will be initialized automatically using the `init.sql` file located in the `infra/postgres` directory.

5. **RabbitMQ Setup**:
   RabbitMQ will be set up with the default credentials:
   - Username: `guest`
   - Password: `guest`

6. **MinIO Setup**:
   MinIO will be initialized with the necessary buckets as defined in `init-buckets.sh`.

## Running the Demo

1. **User Requests an Ambulance**:
   - Navigate to the User screen on the frontend.
   - Fill in the required details to request an ambulance and share your location.

2. **Ambulance Response Team Notification**:
   - The ambulance team will receive a notification and can acknowledge the request.

3. **Traffic Control Notification**:
   - The traffic control team will be notified and can simulate video detection by uploading videos.

4. **Hospital Notification**:
   - The hospital will receive patient information and can prepare accordingly.

## Endpoints Overview

### Backend Endpoints

- **User Endpoints**:
  - `POST /api/v1/users/request`: Request an ambulance.
  
- **Ambulance Endpoints**:
  - `GET /api/v1/ambulance/notifications`: Get notifications for ambulance requests.

- **Traffic Control Endpoints**:
  - `POST /api/v1/traffic/notify`: Notify traffic control of an ambulance request.

- **Hospital Endpoints**:
  - `GET /api/v1/hospital/notifications`: Get notifications for incoming patients.

## Architecture Overview

- **Frontend**: Angular application for user interaction.
- **Backend**: FastAPI application handling business logic and API endpoints.
- **Database**: PostgreSQL for data storage.
- **Message Broker**: RabbitMQ for handling asynchronous notifications.
- **Object Storage**: MinIO for storing uploaded files and videos.
- **Background Tasks**: Celery for processing tasks in the background.

## Conclusion

Follow these instructions to set up and run the AI-Based Green Corridor System for Ambulances. If you encounter any issues, please refer to the README.md file for additional information or troubleshooting tips.
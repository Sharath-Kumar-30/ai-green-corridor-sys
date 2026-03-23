import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ApiService {
  private baseUrl = 'http://localhost:8000/api/v1';

  constructor(private http: HttpClient) {}

  requestAmbulance(data: any): Observable<any> {
    return this.http.post(`${this.baseUrl}/users/request-ambulance`, {
      user_id: 1,
      location: data.location,
      images: [],
      documents: []
    });
  }

  getAmbulanceNotifications(): Observable<any> {
    return this.http.get(`${this.baseUrl}/ambulance/notifications`);
  }

  acknowledgeAmbulanceRequest(requestId: string): Observable<any> {
    return this.http.post(`${this.baseUrl}/ambulance/notify`, {
      request_id: requestId,
      message: 'Ambulance acknowledged'
    });
  }

  sendTrafficSignal(requestId: string): Observable<any> {
    return this.http.post(`${this.baseUrl}/ambulance/notify`, {
      request_id: requestId,
      message: 'Traffic signal activated'
    });
  }

  getTrafficControlUpdates(): Observable<any> {
    return this.http.get(`${this.baseUrl}/traffic/status`);
  }

  getHospitalNotifications(): Observable<any> {
    return this.http.get(`${this.baseUrl}/hospital/notifications`);
  }

  uploadVideo(data: FormData): Observable<any> {
    return this.http.post(`${this.baseUrl}/traffic/traffic-control`, {
      video_file: 'uploaded_video',
      ambulance_request_id: '1'
    });
  }

  uploadFile(data: FormData): Observable<any> {
    return this.http.post(`${this.baseUrl}/hospital/notify`, {
      request_id: '1',
      symptoms: 'Emergency',
      location: 'Hospital',
      documents: []
    });
  }

  getPatientData(patientId: string): Observable<any> {
    return this.http.get(`${this.baseUrl}/hospital/status/${patientId}`);
  }
}
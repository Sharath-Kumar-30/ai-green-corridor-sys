import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ApiService {
  private baseUrl = 'http://localhost:8000/api/v1'; // Adjust the base URL as needed

  constructor(private http: HttpClient) {}

  requestAmbulance(data: any): Observable<any> {
    return this.http.post(`${this.baseUrl}/users/request`, data);
  }

  getAmbulanceNotifications(): Observable<any> {
    return this.http.get(`${this.baseUrl}/ambulance/notifications`);
  }

  getTrafficControlUpdates(): Observable<any> {
    return this.http.get(`${this.baseUrl}/traffic/updates`);
  }

  getHospitalNotifications(): Observable<any> {
    return this.http.get(`${this.baseUrl}/hospital/notifications`);
  }

  uploadVideo(data: FormData): Observable<any> {
    return this.http.post(`${this.baseUrl}/traffic/upload-video`, data);
  }

  getPatientData(patientId: string): Observable<any> {
    return this.http.get(`${this.baseUrl}/hospital/patient/${patientId}`);
  }
}
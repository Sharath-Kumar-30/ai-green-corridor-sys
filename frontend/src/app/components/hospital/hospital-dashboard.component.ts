import { Component, OnInit } from '@angular/core';
import { ApiService } from '../../services/api.service';

@Component({
  selector: 'app-hospital-dashboard',
  templateUrl: './hospital-dashboard.component.html',
  styleUrls: ['./hospital-dashboard.component.css']
})
export class HospitalDashboardComponent implements OnInit {
  notifications: any[] = [];
  patientData: any[] = [];

  constructor(private apiService: ApiService) {}

  ngOnInit(): void {
    this.getNotifications();
    this.getPatientData();
  }

  getNotifications(): void {
    this.apiService.getHospitalNotifications().subscribe(
      (data) => {
        this.notifications = data;
      },
      (error) => {
        console.error('Error fetching notifications', error);
      }
    );
  }

  getPatientData(): void {
    this.apiService.getPatientData().subscribe(
      (data) => {
        this.patientData = data;
      },
      (error) => {
        console.error('Error fetching patient data', error);
      }
    );
  }
}
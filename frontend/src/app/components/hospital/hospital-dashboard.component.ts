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
  uploadedFile: File | null = null;
  responseMessage: string = '';

  constructor(private apiService: ApiService) {}

  ngOnInit(): void {
    this.getNotifications();
  }

  getNotifications(): void {
    this.apiService.getHospitalNotifications().subscribe(
      (data: any) => {
        this.notifications = Array.isArray(data) ? data : [];
      },
      (error: any) => {
        console.error('Error fetching notifications', error);
      }
    );
  }

  onFileChange(event: any): void {
    this.uploadedFile = event.target.files[0];
  }

  onSubmit(): void {
    if (!this.uploadedFile) {
      this.responseMessage = 'Please select a file';
      return;
    }

    const formData = new FormData();
    formData.append('file', this.uploadedFile);

    this.apiService.uploadFile(formData).subscribe(
      (response: any) => {
        this.responseMessage = 'File uploaded successfully!';
        console.log('File uploaded:', response);
      },
      (error: any) => {
        this.responseMessage = 'Error uploading file';
        console.error('Error uploading file:', error);
      }
    );
  }
}
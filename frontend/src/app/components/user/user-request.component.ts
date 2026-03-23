import { Component } from '@angular/core';
import { ApiService } from '../../services/api.service';

@Component({
  selector: 'app-user-request',
  templateUrl: './user-request.component.html',
  styleUrls: ['./user-request.component.css']
})
export class UserRequestComponent {
  ambulanceRequestId: string = '';
  location: string = '';
  videoFile: File | null = null;
  responseMessage: string = '';

  constructor(private apiService: ApiService) {}

  onSubmit() {
    this.requestAmbulance();
  }

  requestAmbulance() {
    const requestData = {
      requestId: this.ambulanceRequestId,
      location: this.location,
      video: this.videoFile
    };

    this.apiService.requestAmbulance(requestData).subscribe(
      (response: any) => {
        this.responseMessage = 'Ambulance requested successfully!';
        console.log('Ambulance requested:', response);
      }, 
      (error: any) => {
        this.responseMessage = 'Error requesting ambulance';
        console.error('Error requesting ambulance:', error);
      }
    );
  }

  onFileChange(event: any) {
    this.videoFile = event.target.files[0];
  }
}
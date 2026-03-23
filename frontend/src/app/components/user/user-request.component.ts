import { Component } from '@angular/core';
import { ApiService } from '../../services/api.service';

@Component({
  selector: 'app-user-request',
  templateUrl: './user-request.component.html',
  styleUrls: ['./user-request.component.css']
})
export class UserRequestComponent {
  ambulanceRequestId: string;
  location: string;
  videoFile: File | null = null;

  constructor(private apiService: ApiService) {}

  requestAmbulance() {
    const requestData = {
      requestId: this.ambulanceRequestId,
      location: this.location,
      video: this.videoFile
    };

    this.apiService.requestAmbulance(requestData).subscribe(response => {
      console.log('Ambulance requested:', response);
    }, error => {
      console.error('Error requesting ambulance:', error);
    });
  }

  onFileChange(event: any) {
    this.videoFile = event.target.files[0];
  }
}
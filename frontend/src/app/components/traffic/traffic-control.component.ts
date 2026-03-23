import { Component } from '@angular/core';
import { ApiService } from '../../services/api.service';

@Component({
  selector: 'app-traffic-control',
  templateUrl: './traffic-control.component.html',
  styleUrls: ['./traffic-control.component.css']
})
export class TrafficControlComponent {
  ambulanceRequestId: string = '';
  location: string = '';
  videoUpload: File | null = null;
  normalTrafficVideo: File | null = null;
  detectionResult: string = '';

  constructor(private apiService: ApiService) {}

  onVideoUpload(event: Event): void {
    const input = event.target as HTMLInputElement;
    if (input.files && input.files.length > 0) {
      this.videoUpload = input.files[0];
    }
  }

  onNormalTrafficVideoUpload(event: Event): void {
    const input = event.target as HTMLInputElement;
    if (input.files && input.files.length > 0) {
      this.normalTrafficVideo = input.files[0];
    }
  }

  analyzeVideos(): void {
    if (this.videoUpload) {
      const formData = new FormData();
      formData.append('video', this.videoUpload);

      this.apiService.uploadVideo(formData).subscribe(
        (response: any) => {
          this.detectionResult = response.message || 'Video processed successfully';
          console.log('Video analysis result:', response);
        },
        (error: any) => {
          this.detectionResult = 'Error processing video';
          console.error('Error uploading video:', error);
        }
      );
    }
  }
}
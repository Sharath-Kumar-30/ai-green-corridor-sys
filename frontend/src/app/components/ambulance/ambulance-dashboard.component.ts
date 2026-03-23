import { Component, OnInit } from '@angular/core';
import { ApiService } from '../../services/api.service';

@Component({
  selector: 'app-ambulance-dashboard',
  templateUrl: './ambulance-dashboard.component.html',
  styleUrls: ['./ambulance-dashboard.component.css']
})
export class AmbulanceDashboardComponent implements OnInit {
  ambulanceRequests: any[] = [];
  selectedRequest: any;

  constructor(private apiService: ApiService) {}

  ngOnInit(): void {
    this.fetchAmbulanceRequests();
  }

  fetchAmbulanceRequests(): void {
    this.apiService.getAmbulanceNotifications().subscribe(
      (data: any) => {
        this.ambulanceRequests = Array.isArray(data) ? data : [];
      },
      (error: any) => {
        console.error('Error fetching ambulance requests', error);
      }
    );
  }

  acknowledgeRequest(requestId: string): void {
    this.apiService.acknowledgeAmbulanceRequest(requestId).subscribe(
      (response: any) => {
        console.log('Request acknowledged', response);
        this.fetchAmbulanceRequests();
      },
      (error: any) => {
        console.error('Error acknowledging request', error);
      }
    );
  }

  sendTrafficSignal(requestId: string): void {
    this.apiService.sendTrafficSignal(requestId).subscribe(
      (response: any) => {
        console.log('Traffic signal sent', response);
      },
      (error: any) => {
        console.error('Error sending traffic signal', error);
      }
    );
  }
}
  }
}
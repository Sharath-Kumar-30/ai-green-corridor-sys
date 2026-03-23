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
    this.apiService.getAmbulanceRequests().subscribe(
      (data: any[]) => {
        this.ambulanceRequests = data;
      },
      (error) => {
        console.error('Error fetching ambulance requests', error);
      }
    );
  }

  acknowledgeRequest(requestId: string): void {
    this.apiService.acknowledgeAmbulanceRequest(requestId).subscribe(
      (response) => {
        console.log('Request acknowledged', response);
        this.fetchAmbulanceRequests(); // Refresh the list
      },
      (error) => {
        console.error('Error acknowledging request', error);
      }
    );
  }

  sendTrafficSignal(requestId: string): void {
    this.apiService.sendTrafficSignal(requestId).subscribe(
      (response) => {
        console.log('Traffic signal sent', response);
      },
      (error) => {
        console.error('Error sending traffic signal', error);
      }
    );
  }
}
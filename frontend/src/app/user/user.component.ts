import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';

const API = (window as any).env?.API_URL || 'http://localhost:8000/api';

@Component({
  selector: 'app-user',
  template: `
    <div>
      <button (click)="newRequest()">New Request</button>
      <button (click)="seed()">Seed Sample</button>
      <div *ngFor="let r of requests" style="border:1px solid #ccc;padding:8px;margin:8px;">
        <div><b>ID:</b> {{r.id}} | <b>Loc:</b> {{r.location}} | <b>Status:</b> {{r.status}} | <b>Green:</b> {{r.green_route ? '✅' : '❌'}}</div>
        <div>{{r.notes}} by {{r.user_name}}</div>
        <button (click)="ack(r.id)">Acknowledge</button>
        <input type="file" (change)="upload($event, r.id)" />
      </div>
    </div>
  `
})
export class UserComponent implements OnInit {
  requests: any[] = [];
  constructor(private http: HttpClient) {}
  ngOnInit(){ this.refresh(); }
  async refresh(){ this.requests = await this.http.get<any[]>(`${API}/requests`).toPromise(); }
  async newRequest(){ const loc = prompt('Location coords (lat,lng)','12.9716,77.5946'); if(!loc) return; await this.http.post(`${API}/requests`, { user_name: 'DemoUser', location: loc, notes: 'Demo' }).toPromise(); this.refresh(); }
  async seed(){ await this.http.post(`${API}/requests`, { user_name: 'Seed', location: '12.944,77.64', notes: 'seed' }).toPromise(); this.refresh(); }
  async ack(id:number){ await this.http.post(`${API}/requests/${id}/ack`, {}).toPromise(); this.refresh(); }
  async upload(ev:any, id:number){ const f = ev.target.files[0]; const fd = new FormData(); fd.append('file', f); await this.http.post(`${API}/requests/${id}/upload`, fd).toPromise(); alert('Uploaded. Wait a few seconds and refresh.'); }
}

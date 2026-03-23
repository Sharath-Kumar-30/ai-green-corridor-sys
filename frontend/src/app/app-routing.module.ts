import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { UserRequestComponent } from './components/user/user-request.component';
import { AmbulanceDashboardComponent } from './components/ambulance/ambulance-dashboard.component';
import { TrafficControlComponent } from './components/traffic/traffic-control.component';
import { HospitalDashboardComponent } from './components/hospital/hospital-dashboard.component';

const routes: Routes = [
  { path: '', redirectTo: '/user-request', pathMatch: 'full' },
  { path: 'user-request', component: UserRequestComponent },
  { path: 'ambulance-dashboard', component: AmbulanceDashboardComponent },
  { path: 'traffic-control', component: TrafficControlComponent },
  { path: 'hospital-dashboard', component: HospitalDashboardComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
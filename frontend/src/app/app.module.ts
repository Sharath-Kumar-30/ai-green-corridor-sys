import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';
import { AppRoutingModule } from './app-routing.module';

import { AppComponent } from './app.component';
import { UserRequestComponent } from './components/user/user-request.component';
import { AmbulanceDashboardComponent } from './components/ambulance/ambulance-dashboard.component';
import { HospitalDashboardComponent } from './components/hospital/hospital-dashboard.component';
import { TrafficControlComponent } from './components/traffic/traffic-control.component';

@NgModule({
  declarations: [
    AppComponent,
    UserRequestComponent,
    AmbulanceDashboardComponent,
    HospitalDashboardComponent,
    TrafficControlComponent
  ],
  imports: [
    BrowserModule,
    FormsModule,
    HttpClientModule,
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule {}
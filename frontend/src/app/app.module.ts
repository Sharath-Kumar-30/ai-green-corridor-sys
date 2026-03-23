import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';
import { RouterModule, Routes } from '@angular/router';

import { AppComponent } from './app.component';

import { UserComponent } from './components/user/user.component';
import { AmbulanceComponent } from './components/ambulance/ambulance.component';
import { HospitalComponent } from './components/hospital/hospital.component';
import { TrafficComponent } from './components/traffic/traffic.component';

const routes: Routes = [];

@NgModule({
  declarations: [
    AppComponent,
    UserComponent,
    AmbulanceComponent,
    HospitalComponent,
    TrafficComponent
  ],
  imports: [
    BrowserModule,
    FormsModule,
    HttpClientModule,
    RouterModule.forRoot(routes)
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule {}
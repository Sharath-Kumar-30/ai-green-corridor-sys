import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  template: `
    <div style="font-family: Arial, sans-serif; padding: 16px;">
      <h1>AI Green Corridor - Demo</h1>
      <nav>
        <a routerLink="/">User</a> | 
        <a routerLink="/ambulance">Ambulance</a> |
        <a routerLink="/traffic">Traffic</a> |
        <a routerLink="/hospital">Hospital</a>
      </nav>
      <router-outlet></router-outlet>
    </div>
  `
})
export class AppComponent {}

import { Component, NgModule } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { HeaderComponent } from './shared/components/header/header.component';
import { ContactoComponent } from './pages/contacto/contacto.component';

import { FooterComponent } from './shared/footer/footer.component';


import { LandingComponent } from './landing/landing.component';

import { ProductosComponent } from './productos/productos.component';

import { DashboardComponent } from './dashboard/dashboard.component';
import { LoginComponent } from './login/login.component';
import { RegistroComponent } from './registro/registro.component';


@Component({
  selector: 'app-root',
  standalone: true,

  imports: [ RouterOutlet, HeaderComponent, DashboardComponent, LandingComponent, ProductosComponent,FooterComponent, ContactoComponent, LoginComponent, RegistroComponent],


  templateUrl: './app.component.html',
  styleUrl: './app.component.css',
})
export class AppComponent {
  title = 'DressCode2024';
}

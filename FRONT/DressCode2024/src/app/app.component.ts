import { Component, NgModule } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { HeaderComponent } from './shared/header/header.component';
import { ContactoComponent } from './pages/contacto/contacto.component';

import { FooterComponent } from './shared/footer/footer.component';


import { LandingComponent } from './pages/landing/landing.component';

import { ProductosComponent } from './pages/productos/productos.component';

import { DashboardComponent } from './pages/dashboard/dashboard.component';
import { LoginComponent } from './pages/login/login.component';
//import { RegistroComponent } from './pages/registro/registro.component';

import { FontAwesomeModule } from '@fortawesome/angular-fontawesome';
import { SobreNosotrosComponent } from './pages/sobre-nosotros/sobre-nosotros.component';

@Component({
  selector: 'app-root',
  standalone: true,
  

imports: [RouterOutlet,HeaderComponent, DashboardComponent, LandingComponent, ProductosComponent,FooterComponent, ContactoComponent,FontAwesomeModule, SobreNosotrosComponent, LoginComponent, ], // RegistroComponent



  templateUrl: './app.component.html',
  styleUrl: './app.component.css',
})
export class AppComponent {
  title = 'DressCode2024';
}

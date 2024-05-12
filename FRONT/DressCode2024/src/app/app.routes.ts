import { Routes } from '@angular/router';

import { ContactoComponent } from './pages/contacto/contacto.component';


import { DashboardComponent } from './dashboard/dashboard.component';

import { ProductosComponent } from './productos/productos.component';
import { LandingComponent } from './landing/landing.component';
import { Pagina404Component } from './pagina404/pagina404.component';
export 

    const routes: Routes = [
        //{path: "", component:  }, //InicioComponent
        {path: "productos", component: ProductosComponent},
        {path:"mis-compras", component:DashboardComponent},
        //{path: "products/:category/:productId", component: ProductDetailComponent},
        { path: 'Contacto', component: ContactoComponent },
        //{path: "**", redirectTo: "", pathMatch: "full"}
        {path: "index", component: LandingComponent},
        {path:"", redirectTo:"/index", pathMatch:"full"},





        //este ruteo a esta pagina404 va a al ultimo
        {path: "**", component: Pagina404Component},
      
        //este ruteo a esta pagina404 va a al ultimo
        
      

];

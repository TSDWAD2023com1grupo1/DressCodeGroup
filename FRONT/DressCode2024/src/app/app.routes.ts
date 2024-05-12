import { Routes } from '@angular/router';
import { DashboardComponent } from './dashboard/dashboard.component';

import { ProductosComponent } from './productos/productos.component';
import { LandingComponent } from './landing/landing.component';
export 

    const routes: Routes = [
        //{path: "", component:  }, //InicioComponent
        {path: "productos", component: ProductosComponent},
        {path:"mis-compras", component:DashboardComponent},
        //{path: "products/:category/:productId", component: ProductDetailComponent},
        //{path: "contact", component: ContactComponent},
        //{path: "**", redirectTo: "", pathMatch: "full"}
          {path: "index", component: LandingComponent},
      
        //HOLA HOLA
        
      
];


import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Producto, productoService } from '../../service/producto.service'; // Importa correctamente
import { HttpClientModule } from '@angular/common/http';


@Component({
  selector: 'app-productos',
  standalone: true,
  
  imports: [CommonModule, HttpClientModule],
  templateUrl: './productos.component.html',
  styleUrls: ['./productos.component.css'], // styleUrl -> styleUrls
})
export class ProductosComponent implements OnInit {
  productos: Producto[] = [];
  @Injectable(productoService : ProductoService)
  constructor() { }


  ngOnInit(): void {
    this.productoService.obtenerProductos()
      .subscribe(productos => this.productos = productos);
  }
}


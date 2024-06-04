import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import {  ProductoService } from '../../service/producto.service';
import { HttpClientModule } from '@angular/common/http';
import { Producto } from '../../models/Producto'


@Component({
  selector: 'app-productos',
  standalone: true,

  imports: [CommonModule, HttpClientModule],
  templateUrl: './productos.component.html',
  styleUrls: ['./productos.component.css'], // styleUrl -> styleUrls
})
export class ProductosComponent implements OnInit {
  productos: any;
    constructor(productoService:ProductoService) { 

      this.productos = productoService.obtenerProductos().subscribe({next: (productos) => {
        this.productos=productos;
      },
        error: (error) => {
        console.error(error)
      }


      });


    }


  ngOnInit(): void {

  }
}
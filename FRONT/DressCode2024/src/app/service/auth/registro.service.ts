import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { Usuario } from '../../models/Usuarios';

@Injectable({
  providedIn: 'root'
})
export class RegistroService {
  url="http://localhost:3000/usuario";
  constructor(private http:HttpClient,) { 
    
    this.http.post<Usuario>(this.url, Usuario);
    this.http.get(this.url)
  }
  crearUsuario(usuario:Usuario):Observable<any>{
    return this.http.post(this.url, usuario);
    
  }

}




/* ABAJO SE ENCUENTRA EL SERVICIO CONECTADO A LA API DJANGO Y FUNCIONANDO*/


/*
import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { Usuario } from '../../models/Usuarios';





@Injectable({
  providedIn: 'root'
})
export class RegistroService {
  url="http://localhost:8000/api/v1usuarios/";
  constructor(private http:HttpClient,) { 
    
    this.http.post<Usuario>(this.url, Usuario);
    this.http.get(this.url)
  }
  crearUsuario(usuario:Usuario):Observable<any>{
    return this.http.post(this.url, usuario);
    
  }

}
*/
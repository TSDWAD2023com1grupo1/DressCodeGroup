import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class UsuarioService {

  constructor(private http:HttpClient) { 
    //this.http.get("https://url-api-rest");
   // this.http.post<Usuario>("https://url-api-rest0", usuario);
    //this.http.put<Usuario>("https://url-api-rest", usuario);


  }
}

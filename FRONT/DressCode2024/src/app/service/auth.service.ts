import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  url="https://reqres.in/api/users/1"; //Devuelve un usuario de

constructor(private http:HttpClient) {
  
 }

 createUser(user:User):Observable<any>
  
}


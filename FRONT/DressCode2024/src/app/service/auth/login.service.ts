import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { BehaviorSubject, Observable, tap, catchError, of } from 'rxjs';
import { throwError } from 'rxjs';
import Swal from 'sweetalert2';
import { Usuario } from '../../models/LoginRequest'; // Asegúrate de importar el modelo Usuario

@Injectable({
  providedIn: 'root'
})
export class LoginService {
  url = "http://localhost:8000/api/v1usuarios/";
  private isLogginOn = new BehaviorSubject<boolean>(false);

  constructor(private http: HttpClient) {}

  login(usuario: Usuario): Observable<any> {
    return this.http.post<{ authenticated: boolean }>(this.url, usuario)
      .pipe(
        tap(response => {
          if (response.authenticated) {
            console.log("Login successful:", response);
            this.isLogginOn.next(true);
            
          } else {
            console.error("Authentication failed");
            this.isLogginOn.next(false);
          }
        }),
        catchError(error => {
          console.error("Login error:", error);
          this.isLogginOn.next(false);
          return of(error);
        })
      );
  }

  get estaAutenticado(): boolean {
    return this.isLogginOn.value;
  }

  get isLogginOn$(): Observable<boolean> {
    return this.isLogginOn.asObservable();
  }
  logOut() {
    this.isLogginOn.next(false); 
  }
}

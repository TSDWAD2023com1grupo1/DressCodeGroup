import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { BehaviorSubject, Observable, of, throwError } from 'rxjs';
import { catchError, map, tap } from 'rxjs/operators';
import Swal from 'sweetalert2';
import { Usuario } from '../../models/LoginRequest'; // Asegúrate de importar el modelo Usuario

@Injectable({
  providedIn: 'root'
})
export class LoginService {
  url = "http://localhost:3000/usuario";
  private isLogginOn = new BehaviorSubject<boolean>(false);

  constructor(private http: HttpClient) {}

  login(usuario: Usuario): Observable<boolean> {
    return this.http.get<Usuario[]>(`${this.url}?email=${usuario.email}&& password=${usuario.password}`)
      .pipe(
        map(users => {
          if (users.length > 0) {
            console.log("Login successful:", users[0]);
            this.isLogginOn.next(true);
           
            return true;
          } else {
            console.error("Authentication failed");
            this.isLogginOn.next(false);
            return false;
          }
        }),
        catchError(error => {
          console.error("Login error:", error);
          this.isLogginOn.next(false);
          return of(false);
        })
      );
  }

  get authenticated(): boolean {
    return this.isLogginOn.value;
  }

  get isLogginOn$(): Observable<boolean> {
    return this.isLogginOn.asObservable();
  }

  logOut() {
    this.isLogginOn.next(false); 
  }
}


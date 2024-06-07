import { Component } from '@angular/core';
import { FormBuilder, FormGroup, ReactiveFormsModule, Validators } from '@angular/forms';
import { LoginService } from '../../service/auth/login.service';
import { Router } from '@angular/router';
import { Usuario } from '../../models/Usuarios';



@Component({
  selector: 'app-login',
  standalone: true,
  imports: [ReactiveFormsModule],
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent {
  form: FormGroup;

  constructor(private formBuilder: FormBuilder,
              private loginService: LoginService,
              private router: Router) {
    this.form = this.formBuilder.group({
      email: ['', [Validators.required, Validators.email]],
      password: ['', [Validators.required, Validators.minLength(8)]]
    });
  }

  onEnviar(event: Event) {
    event.preventDefault();
    this.loginService.login(this.form.value).subscribe({
      next: (authenticated) => {
        if (authenticated) {
          console.log("Se dio acceso");
          if(this.loginService.estaAutenticado)
            alert("Ingreso Correcto!"),
            setTimeout(() => {
              this.router.navigateByUrl("/index")
            }, 3000);;
        } else {
          alert("Credenciales incorrectas");
        }
      },
      error: (error) => {
        console.error("Error durante el login:", error);
        alert("ERROR: " + error.message);
      }
    });
  }

  get Password() {
    return this.form.get('password');
  }

  get Email() {
    return this.form.get('email');
  }

 
 }
  
  
  

 

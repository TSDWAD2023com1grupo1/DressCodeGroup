import { Component } from '@angular/core';
import { FormBuilder, FormGroup, ReactiveFormsModule, Validators } from '@angular/forms';
import { LoginService } from '../../service/auth/login.service';
import { Router } from '@angular/router';
import { Usuario } from '../../models/LoginRequest';

@Component({
  selector: 'app-login',
  standalone: true,
  imports: [ReactiveFormsModule],
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent {
  form: FormGroup;

  constructor(
    private formBuilder: FormBuilder,
    private loginService: LoginService,
    private router: Router
  ) {
    this.form = this.formBuilder.group({
      email: ['', [Validators.required, Validators.email]],
      password: ['', [Validators.required, Validators.minLength(8)]]
    });
  }

  onEnviar(event: Event) {
    event.preventDefault();
    if (this.form.valid) {
      const { email, password } = this.form.value as Usuario;
      this.loginService.login({ email, password }).subscribe({
        next: (authenticated) => {
          if (authenticated) {
            console.log("Login successful");
            alert("Ingreso Correcto!");
            setTimeout(() => {
              this.router.navigateByUrl("/index");
            }, 3000);
          } 
        },
        error: (error) => {
          console.error("Error durante el login:", error);
          alert("ERROR: " + error.message);
        }
      });
    } else {
      this.form.markAllAsTouched();
    }
  }

  get Password() {
    return this.form.get('password');
  }

  get Email() {
    return this.form.get('email');
  }
}




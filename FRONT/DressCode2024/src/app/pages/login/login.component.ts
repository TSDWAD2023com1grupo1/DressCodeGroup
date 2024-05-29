import { Component } from '@angular/core';
import {
  ReactiveFormsModule,
  FormBuilder,
  Validators,
  FormGroup,
} from '@angular/forms';
import { Router, Routes } from '@angular/router';
import { LoginService } from '../../service/auth/login.service';
import { LoginRequest } from '../../service/auth/loginRequest';
import { Subscriber } from 'rxjs';

@Component({
  selector: 'app-login',
  standalone: true,
  imports: [ReactiveFormsModule],
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css'],
})
export class LoginComponent {
  form!: FormGroup;
  constructor(
    private formBuilder: FormBuilder,
    private router: Router,
    private loginService: LoginService
  ) {
    this.form = this.formBuilder.group({
      email: ['cris@gmail.com', [Validators.required, Validators.email]],
      password: ['', Validators.required],
    });
  }

  onEnviar(event: Event) {
    console.log(this.form.value);
  }

  get Password() {
    return this.form.get('password');
  }

  get Email() {
    return this.form.get('email');
  }

  login() {
    if (this.form.valid) {
      this.loginService.login(this.form.value as LoginRequest).subscribe({
        next: (userData) => {
          console.log(userData);
        },
        error: (errorData) => {
          console.error(errorData);
        },
        complete: () => {
          console.info('El login esta completo');
        },
      });
      this.router.navigateByUrl('/mis-compras');
      this.form.reset();
    } else {
      this.form.markAllAsTouched();
      alert('Se cometio un error al ingresar los datos');
    }
  }
}

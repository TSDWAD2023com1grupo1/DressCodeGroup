import { Component } from '@angular/core';

import { ReactiveFormsModule, FormBuilder, Validators, FormGroup, AbstractControl } from '@angular/forms';
import { AuthService } from '../../services/auth.service';

// import { User } from '../../../models/user';

@Component({
  selector: 'app-registro',
  standalone: true,
  imports: [ReactiveFormsModule],
  templateUrl: './registro.component.html',
  styleUrl: './registro.component.css'
})
export class RegistroComponent {
  

  
  
   
      formRegister!:FormGroup;
      constructor(private formBuilder: FormBuilder ) //private authService:AuthServicevice, private router: Router
      {
    
    
        this.formRegister=this.formBuilder.group(
              {
                nombre:["",[
                  Validators.required,
                  Validators.minLength(3),
                  Validators.pattern(/^[a-zA-ZñÑáéíóúÁÉÍÓÚ\s]+$/)]],

                email:["",[
                  Validators.required, 
                  Validators.email]],

                password:["",[
                  Validators.required,
                  Validators.minLength(8), 
                  Validators.maxLength(16), 
                  Validators.pattern(/^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*\W)/)]],
                repitePassword: [
                  "", 
                  Validators.required
                ]
              },
              {
                validator: this.passwordMatchValidator
              }
        );
       
        
      
      }

      passwordMatchValidator(control: AbstractControl) {

        const password = control.get('password')?.value;
        const repitePassword = control.get('repitePassword')?.value;
        return password === repitePassword ? null : { mismatch: true };
      }
      
      onEnviar(event:Event) {
        event.preventDefault();
        if (this.formRegister.valid) {
          console.log(this.formRegister.value);
       } 
        else {
          this.formRegister.markAllAsTouched(); 
      }
    }

    //this.authService.createUser(this.form.value)
    
    
    
      get Password(){
        return this.formRegister.get("password");}
      
      get Email(){
        return this.formRegister.get("email");
      }
      get Nombre(){
        return this.formRegister.get("nombre");}
      
      get RepitePassword(){
        return this.formRegister.get("repitePassword");
      
    
      
    
    
    }
    
}
    
  
   
  

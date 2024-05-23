import { Component } from '@angular/core';

import { ReactiveFormsModule, FormBuilder, Validators, FormGroup } from '@angular/forms';

@Component({
  selector: 'app-registro',
  standalone: true,
  imports: [ReactiveFormsModule],
  templateUrl: './registro.component.html',
  styleUrl: './registro.component.css'
})
export class RegistroComponent {
  

  
  
   
      formRegister!:FormGroup;
      constructor(private formBuilder: FormBuilder){
    
    
        this.formRegister=this.formBuilder.group(
              {
                nombre:["",[Validators.required,Validators.minLength(3),Validators.pattern(/^[a-zA-ZñÑáéíóúÁÉÍÓÚ\s]+$/)]],
                email:["",[Validators.required, Validators.email]],
                password:["",[Validators.required,Validators.minLength(8), Validators.maxLength(16), Validators.pattern(/^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*\W).{8,16}$/)]],
                repitePassword:["",[Validators.required, Validators.minLength(8)]]
              }
        )
       
        
      
      }
      
      onEnviar(event:Event)
      {
        console.log(this.formRegister.value)
      }
    
    
    
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
    
  
   
  


import { Component} from '@angular/core';
import { ReactiveFormsModule, FormBuilder, Validators, FormGroup } from '@angular/forms';




@Component({
  selector: 'app-login',
  standalone: true,
  imports: [ReactiveFormsModule, 
  ],
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css',
  ]
})
export class LoginComponent {
 
    
    form!:FormGroup;
    constructor(private formBuilder: FormBuilder){
  
  
      this.form=this.formBuilder.group(
            {
              email:["",[Validators.required, Validators.email]],
              password:["",[Validators.required, Validators.minLength(8)]]
  
            }
      )
     
      
    
    }
    
    onEnviar(event:Event)
    {
      console.log(this.form.value)
    }
  
  
  
    get Password(){
      return this.form.get("password");}
    
    get Email(){
      return this.form.get("email");
    }
    
    
    
  
  
  }
  
  
  

 

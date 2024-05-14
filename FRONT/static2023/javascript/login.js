@ViewChild('signInBtn') signInBtn!: ElementRef;
  @ViewChild('signUpBtn') signUpBtn!: ElementRef;
  @ViewChild('registerForm') registerForm!: ElementRef;
  @ViewChild('loginForm') loginForm!: ElementRef;

  constructor(private renderer: Renderer2) {}

  ngAfterViewInit() {
    const url = window.location.href;
    if (url.includes("login.html")) {
      this.renderer.listen(this.signInBtn.nativeElement, 'click', () => {
        this.renderer.addClass(this.registerForm.nativeElement, 'hide');
        this.renderer.removeClass(this.loginForm.nativeElement, 'hide');
      });

      this.renderer.listen(this.signUpBtn.nativeElement, 'click', () => {
        this.renderer.addClass(this.loginForm.nativeElement, 'hide');
        this.renderer.removeClass(this.registerForm.nativeElement, 'hide');
      });
    }
  }

if(window.location.href.includes("login.html")){

    function registrar(){
        
        let nombre = document.getElementById("name").value;
        let email = document.getElementById("email").value;
        let pass = document.getElementById("clave").value;
        let passrepit = document.getElementById("clave-repite").value;
    
        let warnings = "";
        let entrar = false;
        let regexEmail = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
        let regexNombre = /^[a-zA-ZñÑáéíóúÁÉÍÓÚ\s]+$/;
        let regexContraseña = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*\W).{8,16}$/;
        
        
        if (nombre === "" || email === "" || pass === "") {
            warnings += "Todos los campos son obligatorios.\n"
            entrar = true;
        };
        if(nombre.length < 4){
            warnings += "El nombre no es valido.\n";
            entrar = true;
        };
        if(!regexNombre.test(nombre)) {
            warnings += "El nombre solo debe contener letras.\n";
            entrar = true;
        };
        if (!regexEmail.test(email)) {
            warnings += 'El email ingresado no es válido..\n';
            entrar = true;
        };  
        if(pass.length <8){
            warnings += 'La contraseña debe contener mínimo 8 caracteres.\n';
            entrar = true;
        };
        
        if(pass.length >16){
            warnings += 'La contraseña no puede superar los 16 caracteres.\n';
            entrar = true;
        };
        if(!regexContraseña.test(pass)){
            warnings += 'La contraseña debe contener al menos un número, una letra mayúscula, una letra minúscula y un caracter no alfanumérico.\n';
            entrar = true;
        };
        if( pass !== passrepit){
            warnings += "Las contraseñas no coinciden.\n";
            entrar = true;
        };
        if(entrar) {
            swal(
                tittle = "Error",
                text = warnings,
                icon = "warning",
            );
        }else{
            swal(title= "¡Felicitaciones!",
                 text = "¡Se ha registrado correctamente!",
                 icon = "success"
            );
            
        };
    };
};
    
const modal = document.getElementById('myModal');
const openModalBtn = document.getElementById('openModalBtn');
const formContent = document.querySelector(".container-form");
    
let modalMostrado = false;  
    
    
function mostrarModal() {
    if (!modalMostrado) {
            modal.style.display = 'block';
            modalMostrado = true;  
            setTimeout(function() {
                formContent.classList.remove("hide");
            }, 1000);
    };
};
    
setTimeout(mostrarModal, 2000);

document.getElementById("user-log").addEventListener("click", function(e) {
        e.preventDefault(); 
        
        loguear(); 
    }   
);
    
    
function loguear() {
        let user = document.getElementById("email-login").value;
        let pass = document.getElementById("contraseña").value;  
    
    
        if (user === "Juan@gmail.com" && pass === "1234!Milan") {  
            
            if (window.location.href.includes("login.html")) {
                swal(
                    title="Bienvenido",
                    text="Inicio de sesión exitoso. Redirigiendo a la página...",
                    icon="success",
                );
                setTimeout(function() {
                    window.location.href = "../../index.html";
                }, 4000);
            }
                {
                swal(
                    title="Bienvenido",
                    text="¡Inicio de sesión exitoso!",
                    icon="success",
                );
                modal.style.display = 'none'; 
                setTimeout(function() {
                    }, 4000);
                
            }
        } else {
            if(user != "Juan@gmail.com" || pass != "1234!Milan"){
                swal({
                title:"¡Datos Incorrectos!",
                icon:"error",
            });}
            if(user == "" && pass == ""){
                {swal({
                        title:"¡No se registraron datos!",
                        icon:"warning",
                    });
        
                };
            };
          };
    
};

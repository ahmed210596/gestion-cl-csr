import { Component, OnInit } from '@angular/core';
import { AuthenticationService } from '../authentication.service';
import { StorageService } from '../storage.service';
import { Users } from '../users';
import { AnonymousSubject } from 'rxjs/internal/Subject';
import { FormBuilder, FormGroup, Validators,FormControl } from '@angular/forms';
import { Router } from '@angular/router';
import jwt_decode from "jwt-decode";
@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {
  loginForm!: FormGroup;
  
  isLoggedIn = false;
  isLoginFailed = false;
  errorMessage = '';
  roles!: string;
  token: any;
  errors: any[] = [];
  username:any;
  obj!: any;
  
  returnUrl: any;
  loading = false;
  submitted = false;
  decodedToken: any;
  is_superuser: boolean = false;

  constructor(private authService: AuthenticationService,
     private storageService: StorageService,
      private router: Router,private fb:FormBuilder) { }

  ngOnInit(): void {
    if (this.storageService.isLoggedIn()) {
      this.isLoggedIn = true;
      // this.getRole();
    }
    this.loginForm = this.fb.group({
      username:new FormControl('', Validators.required),
      password: new FormControl('', Validators.required)
  });

 

  }
  get f() { return this.loginForm.controls; }

  onSubmit(): void {
    
    this.submitted = true;
    console.log(this.f['username'].value);
    console.log(this.f['password'].value);
    this.authService.signinUser(this.loginForm.value).subscribe({
    
      next: data=> {
        
        
        console.log(data)
        this.storageService.saveUser(data)
        const token =this.storageService.getUser()
        this.decodedToken = jwt_decode(token);
        console.log(this.decodedToken)
        const user_id = this.decodedToken.user_id;
        const email = this.decodedToken.email;
        this.is_superuser = this.decodedToken.is_supeuser;
        console.log(user_id)
        console.log(email)
        console.log(this.is_superuser)
        // this.obj=this.updateData(data.token);
        console.log(data)
        this.isLoginFailed = false;
        this.isLoggedIn = true;
        this.loading = true;
        this.reloadPage();
        this.getRole();
        
        
      },
      error: err => {
        this.errorMessage = err.error.errorMessage;
        console.log(this.errorMessage)
        //this.errorMessage="invalid credential account"
        this.isLoginFailed = true;
        this.errors = err.errorMessage
        this.loading = false;
        
      }
    });
  }

  reloadPage(): void {
    window.location.reload();
  }
  getRole(): void {
    if (this.is_superuser==true){
      this.roles='ROLE_ADMIN';

    }
    this.roles='ROLE_MODERATOR';
  } 

  /* updateData(token:any) {
    this.token = token;
    this.errors = [];
 
    // decode the token to read the username and expiration timestamp
    const token_parts = this.token.split(/\./);
    const token_decoded = JSON.parse(window.atob(token_parts[1]));
    this.username = token_decoded.username;
  } */
}




// signup.component.ts


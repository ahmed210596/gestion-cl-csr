import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';
import { tap } from 'rxjs/operators';
import { Users } from './users';
import { StorageService } from './storage.service';

interface TokenResponse {
  access: string;
  refresh: string;
}

@Injectable({
  providedIn: 'root'
})


export class AuthenticationService {
  // replace with your backend API URL
  httpOptions: { headers: HttpHeaders; };
   
  constructor(private http: HttpClient, private storageService: StorageService) {
    this.httpOptions = {
      headers: new HttpHeaders({'Content-Type': 'application/json'})
    };
 }
  
 private url = 'http://localhost:8000';

signinUser(loginRequest:any) {
    console.log(this.http.post(`${this.url}/login/`, loginRequest))

    return  this.http.post(`${this.url}/login/`, loginRequest);

   

    }
 
 
  register(resgiter_request:any){
    
    return this.http.post(`${this.url}/signup/`, resgiter_request);
  }

  logout(){
    return this.http.get(`${this.url}/logout/`)
    
  }

  isLoggedIn():boolean {
    
    return this.storageService.isLoggedIn();
  }
}

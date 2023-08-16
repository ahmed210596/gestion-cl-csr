import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Users } from './users';

const API_URL = 'http://localhost:8000/';

@Injectable({
  providedIn: 'root',
})
export class UserService {
  constructor(private http: HttpClient) {}

  

  getPublicContent(): Observable<any> {
    return this.http.get(API_URL + 'all');
  }
  
  getModeratorBoard(): Observable<any> {
    return this.http.get(API_URL + 'employer-boards', { responseType: 'text' });
  }

  getAdminBoard(): Observable<any> {
    return this.http.get(API_URL + 'admin-boards', { responseType: 'text' });
  }
  
  updateProfile(id:number,data:any){
    return this.http.put<Users>(API_URL+'update_profile/'+id,data);
  }
  
}


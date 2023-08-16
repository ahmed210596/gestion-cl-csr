import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
@Injectable({
  providedIn: 'root'
})
export class PasswordResetService {

  
  private baseUrl = 'http://127.0.0.1:8000/';

  constructor(private http: HttpClient) { }

  sendPasswordResetEmail(email: string):Observable<any> {
    const url = this.baseUrl + 'send-password-reset-email/';
    const payload = { email };
    return this.http.post(url, payload);
  }
}

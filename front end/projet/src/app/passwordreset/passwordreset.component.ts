import { Component } from '@angular/core';

import { HttpClient } from '@angular/common/http';
@Component({
  selector: 'app-passwordreset',
  templateUrl: './passwordreset.component.html',
  styleUrls: ['./passwordreset.component.css']
})
export class PasswordresetComponent {
  email: string = '';

  constructor(private http: HttpClient) {}

  onSubmit() {
    const url = 'http://127.0.0.1:8000/send-password-reset-email/';
    const body = { email: this.email };
    this.http.post(url, body).subscribe(() => {
      alert('Password reset email sent!');
    }, error => {
      alert('Error sending password reset email!');
    });
  }
}

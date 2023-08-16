import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';
@Component({
  selector: 'app-change-password',
  templateUrl: './change-password.component.html',
  styleUrls: ['./change-password.component.css']
})
export class ChangePasswordComponent {
  oldPassword!: string;
  newPassword!: string;

  constructor(private http: HttpClient) { }

  onSubmit() {
    const data = {
      old_password: this.oldPassword,
      new_password: this.newPassword
    };

    this.http.put('127.0.0.1:8000/change-password/', data).subscribe(
      res => console.log(res),
      err => console.log(err)
    );
  }
}

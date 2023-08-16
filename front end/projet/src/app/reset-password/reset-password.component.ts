import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-reset-password',
  templateUrl: './reset-password.component.html',
  styleUrls: ['./reset-password.component.css']
})
export class ResetPasswordComponent implements OnInit {
  newPassword: string = '';
  confirmPassword: string = '';
  message: string = '';
  uidb64: string | null = null;
  token: string | null = null;

  constructor(private http: HttpClient, private route: ActivatedRoute) {}

  ngOnInit() {
    this.route.params.subscribe(params => {
       this.uidb64 = params['uidb64'];
       this.token = params['token'];
      
      // Use the uidb64 and token values as needed
      
      
      // Call a method or perform actions based on the route parameters
      
    });
  }

  onSubmit() {
    

    const url = `http://localhost:8000/reset-password/${this.uidb64}/${this.token}/`;
    const data = { new_password: this.newPassword, confirm_password: this.confirmPassword };

    this.http.post(url, data).subscribe(
      () => {
        this.message = 'Password reset successful!';
      },
      (error) => {
        this.message = 'Password reset failed.';
      }
    );
  }
}


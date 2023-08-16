import { Component } from '@angular/core';
import { PasswordResetService } from '../password-reset.service';
@Component({
  selector: 'app-password-reset-form',
  templateUrl: './password-reset-form.component.html',
  styleUrls: ['./password-reset-form.component.css']
})
export class PasswordResetFormComponent {
  email!: string;

  constructor(private passwordResetService: PasswordResetService) { }

  submitForm() {
    this.passwordResetService.sendPasswordResetEmail(this.email)
      .subscribe(
        (data) => {
          console.log(data)
          alert('Password reset email sent!');
          
        }, error => {
          alert('Error sending password reset email!');
        }
      );
  }
}

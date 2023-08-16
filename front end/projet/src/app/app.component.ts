import { Component } from '@angular/core';
import { StorageService } from './storage.service';
import { AuthenticationService } from './authentication.service';
import { Router } from '@angular/router';
import jwt_decode from "jwt-decode";
@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  decodedToken: any;
  is_superuser: any;
  title(title: any) {
    throw new Error('Method not implemented.');
  }
  
  roles!: string; 
  isLoggedIn = false;
  showAdminBoard = false;
  showModeratorBoard = false;
  matricule?: string;

  constructor(private storageService: StorageService, private authService: AuthenticationService,private router: Router) { }

  ngOnInit(): void {
    this.isLoggedIn = this.storageService.isLoggedIn();

    if (this.isLoggedIn) {
      const token = this.storageService.getUser();
      this.decodedToken = jwt_decode(token);
        const user_id = this.decodedToken.user_id;
        const email = this.decodedToken.email;
        this.is_superuser = this.decodedToken.is_supeuser;

      // if(this.is_superuser== true ){
      //   this.roles = 'ROLE_ADMIN';
      // }
      // this.roles = 'ROLE_MODERATOR';    
      
      // this.showAdminBoard = this.roles=='ROLE_ADMIN';
      // this.showModeratorBoard = this.roles=='ROLE_MODERATOR';

      this.matricule = this.decodedToken.matricule;
    }
  }

  logout(): void {
    // this.authService.logout().subscribe({
    //   next: () => {
    //     console.log("ahmed")
    //     this.storageService.clean();
    //     setTimeout(() => {
    //       this.router.navigate(['/login']);
    //     }, 3000);
    //   },
    //   error: (err) => {
    //     console.error(err);
    //   }
    // });
    this.storageService.clean(); 
  }
  
  }




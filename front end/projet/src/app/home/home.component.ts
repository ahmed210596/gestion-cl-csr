import { Component, OnInit } from '@angular/core';
import { UserService } from '../user.service';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {
  message?: string;
  author: any;
  version: any;
  status!: string;

  constructor(private userService: UserService) { }

  ngOnInit(): void {
    this.userService.getPublicContent().subscribe({
      next: data => {
        
        this.message = data.message;
        this.author = data.author;
        this.version = data.version; 
        console.log(data)
       

      },
      error: err => {
        if (err.error) {
          console.error('Error fetching data:', err.error);
        } else {
          this.status = "Error with status: " + err.status;
        }
      }
    });
  }
}


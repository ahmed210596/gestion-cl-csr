import { Component, OnInit } from '@angular/core';
import { StorageService } from '../storage.service';
import { JwtHelperService } from '@auth0/angular-jwt';
@Component({
  selector: 'app-profile',
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.css']
})
export class ProfileComponent implements OnInit {
  currentUser: any;

  constructor(private storageService: StorageService,private jwtHelper: JwtHelperService) { }

  ngOnInit(): void {
    const token = this.storageService.getUser();
    if (token) {
      this.currentUser = this.jwtHelper.decodeToken(token);
      return this.currentUser.user_id;
    }
    return ;
  }
}


import { Injectable } from '@angular/core';
import { Users } from './users';
import { Observable } from 'rxjs';

const USER_KEY = 'token';
const userId= 'userID';

@Injectable({
  providedIn: 'root'
})
export class StorageService {
  constructor() {}
  
  clean(): void {
    //localStorage.clear();
    localStorage.removeItem(USER_KEY)
  }

  public saveUser(user: any){
    localStorage.removeItem(USER_KEY);
    
    
    localStorage.setItem(USER_KEY, user.token);
    
    
  }

  public getUser(): any {
    const user = localStorage.getItem(USER_KEY);
    if (user) {
      return user;
    }

    return {};
  }
  
  public isLoggedIn(): boolean {
    const user = localStorage.getItem(USER_KEY);
    if (user) {
      return true;
    }

    return false;
  }
}


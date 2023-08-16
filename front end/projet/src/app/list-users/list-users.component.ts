import { Component, Input, OnInit } from '@angular/core';
import { DataService } from '../data.service';
import { AuthenticationService } from '../authentication.service';
@Component({
  selector: 'app-list-users',
  templateUrl: './list-users.component.html',
  styleUrls: ['./list-users.component.css']
})
export class ListUsersComponent implements OnInit  {
  users:any;
  currentPage = 1;
  pageSize = 3;
  query!: string;
 constructor(private dataservice:DataService,userService:AuthenticationService){
   
 }
 ngOnInit(): void {
  this.fetchUser();
}
deleteUser(id:any){

this.dataservice.delUser(id).subscribe(()=>{
  this.fetchUser();

})
}
fetchUser(){
  this.dataservice.ListUsers(this.currentPage, this.pageSize).subscribe((response)=>{
    this.users=response.results;
    console.log(this.users)
    
    
})
}
nextPage(): void {
  this.currentPage++;
  console.log(this.currentPage)
  this.fetchUser();
}

previousPage(): void {
  if (this.currentPage > 1) {
    this.currentPage--;
    console.log(this.currentPage)
    this.fetchUser();
  }
}
activate(user:any){
  user.is_active =!user.is_active;
  console.log(user.is_active)
  this.dataservice.editUser(user.id,user).subscribe(()=>{
    // key.status = !key.status;
    
    this.fetchUser();
  
  })
  }
searchUsers(){
  this.dataservice.searchUsers(this.query).subscribe((response)=>{
    this.users=response;
    console.log(this.users)
    
    
})
}
}
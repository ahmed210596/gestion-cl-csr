import { Component, OnInit } from '@angular/core';
import { Users } from '../users';
import { UserService } from '../user.service'
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { DataService } from '../data.service';
import { ActivatedRoute } from '@angular/router';
@Component({
  selector: 'app-update-profile',
  templateUrl: './update-profile.component.html',
  styleUrls: ['./update-profile.component.css']
})

export class UpdateProfileComponent implements OnInit {
  
  angForm:FormGroup
  id: any;
  
  
  constructor(private fb:FormBuilder,private DataService:DataService,private route: Router,private ActivatedRoute:ActivatedRoute,UserService:UserService){
    this.angForm=this.fb.group({
      matricule:['',Validators.required],
      username:['',Validators.required],
      email:['',Validators.required],
      
      
    })
    }
  ngOnInit(): void {
    
    this.ActivatedRoute.params.subscribe(paramId=>{
      this.id=paramId['id'];
      this.DataService.getUser(this.id).subscribe(data=>{
        this.angForm?.patchValue(data);
      })
    })
  }
  onSubmit(): void {
    // update the user profile
    this.DataService.editUser(this.id,this.angForm?.value).subscribe(data=>{ 
      this.route.navigate(['list-users']);
    })
  }


}

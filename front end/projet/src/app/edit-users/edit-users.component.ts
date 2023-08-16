import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { DataService } from '../data.service';
import { ActivatedRoute } from '@angular/router';
@Component({
  selector: 'app-edit-users',
  templateUrl: './edit-users.component.html',
  styleUrls: ['./edit-users.component.css']
})
export class EditUsersComponent implements OnInit  {
  angForm:FormGroup
  id: any;
  constructor(private fb:FormBuilder,private DataService:DataService,private route: Router,private ActivatedRoute:ActivatedRoute){this.angForm=this.fb.group({
    matricule:['',Validators.required],
    password:['',Validators.required],
    email:['',Validators.required],
    username:['',Validators.required],
    password_confirm:['',Validators.required],
  })}
    ngOnInit(): void {
      this.ActivatedRoute.params.subscribe(paramId=>{
        this.id=paramId['id'];
        this.DataService.getUser(this.id).subscribe(data=>{
          this.angForm?.patchValue(data);
        })
      })
      
    }
    postdata(){
      console.log(this.angForm.value)
    this.DataService.editUser(this.id,this.angForm?.value).subscribe(data=>{ 
      console.log(data)
      this.route.navigate(['list-users']);
    })
    }
}

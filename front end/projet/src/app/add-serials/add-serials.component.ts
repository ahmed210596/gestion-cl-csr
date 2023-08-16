import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { SerialService } from '../serial.service';
import { ActivatedRoute, Router } from '@angular/router';
import { JwtHelperService } from '@auth0/angular-jwt';

import { MatDialogRef } from '@angular/material/dialog';
@Component({
  selector: 'app-add-serials',
  templateUrl: './add-serials.component.html',
  styleUrls: ['./add-serials.component.css']
})
export class AddSerialsComponent implements OnInit  {
  angForm!: FormGroup;
  constructor(private fb:FormBuilder,private SerialsService:SerialService,private route: Router,private jwtHelper: JwtHelperService,public dialogRef: MatDialogRef<AddSerialsComponent>){}
  ngOnInit(): void {
    this.angForm=this.fb.group({
      serial_number:['',Validators.required],
      creator: [this.getCreatorFromToken(),Validators.required ]
     
      
    });
  }
  getCreatorFromToken():number | null  {
      
    const token = localStorage.getItem('token');
    if (token) {
      const decodedToken = this.jwtHelper.decodeToken(token);
      return decodedToken.user_id;
    }
    return null;
  }
  postdata(){
    this.SerialsService.addSerial(this.angForm.value).subscribe(data=>{ 
      this.route.navigate(['list-serial']);
    });
    }
}

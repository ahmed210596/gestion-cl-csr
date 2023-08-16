import { Component, OnInit } from '@angular/core';
import { KeyCSRService } from '../key-csr.service';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { ProductsService } from '../products.service';
import { ActivatedRoute, Router } from '@angular/router';
import { JwtHelperService } from '@auth0/angular-jwt';
import { HttpRequest } from '@angular/common/http';
@Component({
  selector: 'app-key-csr-list',
  templateUrl: './key-csr-list.component.html',
  styleUrls: ['./key-csr-list.component.css']
})
export class KeyCSRListComponent implements OnInit{
  keys:any;
  angForm!:FormGroup
  id: any;
 constructor(private KeyCSRService:KeyCSRService){}
 ngOnInit(): void {
  this.fetchKey();
}
toggleKeyStatus(key:any){
  key.status =!key.status;
  console.log(key.status)
  
  this.KeyCSRService.changestatuskey(key.id,key).subscribe(()=>{
    // key.status = !key.status;
    
    this.fetchKey();
  
  })
  }
  fetchKey(){
    this.KeyCSRService.listKeys().subscribe((data)=>{
       this.keys=data; 
      
  })
  }

}

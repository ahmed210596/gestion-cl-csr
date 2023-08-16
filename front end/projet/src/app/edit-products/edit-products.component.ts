import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { ProductsService } from '../products.service';
import { ActivatedRoute, Router } from '@angular/router';
import { JwtHelperService } from '@auth0/angular-jwt';
import { HttpRequest } from '@angular/common/http';
@Component({
  selector: 'app-edit-products',
  templateUrl: './edit-products.component.html',
  styleUrls: ['./edit-products.component.css']
})
export class EditProductsComponent implements OnInit{
  angForm!:FormGroup
  id: any;
  constructor(private fb:FormBuilder,private ProductsService:ProductsService,private route: Router,private ActivatedRoute:ActivatedRoute,private jwtHelper: JwtHelperService){
  }
    ngOnInit(): void {
      this.angForm=this.fb.group({
        product_code:['',Validators.required],
        typer:['',Validators.required],
        designation:['',Validators.required],
        
        
      })
      this.ActivatedRoute.params.subscribe(paramId =>{
        this.id=paramId['id'];
        this.ProductsService.getProduct(this.id).subscribe(data=>{
          this.angForm?.patchValue(data);
        })
      })
      
      
    }
    
     
    postdata(){
      console.log(this.angForm.value)
    this.ProductsService.editProduct(this.id,this.angForm?.value).subscribe(data=>{ 
      this.route.navigate(['list-prod']);
    })
    }
}

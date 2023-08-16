import { Component ,Input,OnInit} from '@angular/core';
import { FormGroup,FormBuilder, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { KeyCSRService } from '../key-csr.service'; 
import { Products } from '../products'; 
import { Serial } from '../serial';
import { JwtHelperService } from '@auth0/angular-jwt';

import { ProductsService } from '../products.service';
import { SerialService } from '../serial.service';

@Component({
  selector: 'app-add-csr',
  templateUrl: './add-csr.component.html',
  styleUrls: ['./add-csr.component.css']
})
export class AddCsrComponent implements OnInit{
  angForm!: FormGroup;
  products:any;
  // products: Products[] = [];
  // serials:Serial [] = [];
  serials:any;
  keys:any;
  currentPage = 1;
  pageSize = 3;
constructor(private fb:FormBuilder,private KeyCSRService:KeyCSRService,private route: Router,private productsService: ProductsService,
  private serialsService: SerialService,private jwtHelper: JwtHelperService){}
  ngOnInit(): void {
    this.angForm=this.fb.group({
    serial: ['',Validators.required],  
    product: ['',Validators.required],
    country: ['',Validators.required],
    state: ['',Validators.required],
    locality: ['',Validators.required],
    organization: ['',Validators.required],
    org_unit: ['',Validators.required],
    common_name: ['',Validators.required],
    duree: ['',Validators.required],
     
      
    });
    this.productsService.ListProducts(this.currentPage,
      this.pageSize).subscribe(product => {
      
      this.products=product.results;
      console.log(this.products)
    });

    this.serialsService.ListSerials(this.currentPage,
      this.pageSize).subscribe(serial => {
      
      this.serials=serial.results;
      console.log(this.serials)
    });
  
  }
  
  
  postdata(){
  this.KeyCSRService.addkey(this.angForm.value).subscribe(data=>{ 
    this.route.navigate(['list-csr']);
  });
  }
}

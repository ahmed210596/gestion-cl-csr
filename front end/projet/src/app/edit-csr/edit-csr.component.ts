import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { KeyCSRService } from '../key-csr.service';
import { ActivatedRoute, Router } from '@angular/router';
import { JwtHelperService } from '@auth0/angular-jwt';
import { SerialService } from '../serial.service';
import { ProductsService } from '../products.service';

@Component({
  selector: 'app-edit-csr',
  templateUrl: './edit-csr.component.html',
  styleUrls: ['./edit-csr.component.css']
})
export class EditCsrComponent implements OnInit {
  angForm!:FormGroup
  id: any;
  products:any;
  // products: Products[] = [];
  // serials:Serial [] = [];
  serials:any;
  keys:any;
  currentPage = 1;
  pageSize = 3;
  selectedproductid: any;
  selectedserialid: any;
  selectedproduct: any;
  selectedserial: any;
  selectedserialnum: any;
  selectedproductcode: any;
  constructor(private fb:FormBuilder,private KeyCSRService :KeyCSRService ,private route: Router,private ActivatedRoute:ActivatedRoute,private jwtHelper: JwtHelperService,private productsService: ProductsService,
    private serialsService: SerialService){
   }
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
        
        
      })
      this.ActivatedRoute.params.subscribe(paramId =>{
        this.id=paramId['id'];
        this.KeyCSRService.getkey(this.id).subscribe(data=>{
          this.angForm?.patchValue(data);
          console.log(this.angForm.value)
          this.selectedproductid=this.angForm.value.product.id
          this.selectedserialid=this.angForm.value.serial.id
          this.selectedserialnum=this.angForm.value.serial.serial_number
          this.selectedproductcode=this.angForm.value.product.product_code 
           console.log(this.selectedproductid)
           console.log(this.selectedserialid)
        })
      })
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
    this.KeyCSRService.editkey(this.id,this.angForm?.value).subscribe(data=>{ 
      this.route.navigate(['list-csr']);
    })
    }
}

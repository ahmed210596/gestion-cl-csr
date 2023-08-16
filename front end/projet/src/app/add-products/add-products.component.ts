import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { ProductsService } from '../products.service';
import { JwtHelperService } from '@auth0/angular-jwt';
@Component({
  selector: 'app-add-products',
  templateUrl: './add-products.component.html',
  styleUrls: ['./add-products.component.css']
})
export class AddProductsComponent implements OnInit {
  angForm!: FormGroup;
  currentUser: number | null | undefined;
  constructor(private fb:FormBuilder,private ProductsService:ProductsService,private route: Router,private jwtHelper: JwtHelperService){}
    ngOnInit(): void {
      this.currentUser = this.getCreatorFromToken();
      this.angForm=this.fb.group({
        product_code:['',Validators.required],
        typer:['',Validators.required],
        designation:['',Validators.required],
       
        
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
      
      console.log(this.angForm.value)
    this.ProductsService.addPoduct(this.angForm.value).subscribe(data=>{ 
      this.route.navigate(['/list-prod']);
    });
    }

}

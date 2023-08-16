import { Component } from '@angular/core';
import { ProductsService } from '../products.service'; 
import { MatDialogRef, MAT_DIALOG_DATA } from '@angular/material/dialog';
import {  Inject } from '@angular/core';
import { Router } from '@angular/router';
import { ListProductsComponent } from '../list-products/list-products.component'; 
@Component({
  selector: 'app-delete-dialog-product',
  templateUrl: './delete-dialog-product.component.html',
  styleUrls: ['./delete-dialog-product.component.css'],
  
})
export class DeleteDialogProductComponent {
  constructor(
    public dialogRef: MatDialogRef<DeleteDialogProductComponent>,
    @Inject(MAT_DIALOG_DATA) public data: any,private ProductsService:ProductsService,private router: Router
  ) {}
  confirmDelete(): void {
    console.log(this.data)
    
    this.ProductsService.delProduct(this.data.id).subscribe(() => {
      this.dialogRef.close(true); 
      this.router.navigate(['/list-prod']);
    });
}
}
import { Component, OnInit } from '@angular/core';
import { ProductsService } from '../products.service';
import { AfterViewInit,  ElementRef,  ViewChild } from '@angular/core';
import { DeleteDialogProductComponent } from '../delete-dialog-product/delete-dialog-product.component';
import * as M from 'materialize-css';
import { MatDialog, MatDialogRef } from '@angular/material/dialog';
import { AddProductsComponent } from '../add-products/add-products.component';
@Component({
  selector: 'app-list-products',
  templateUrl: './list-products.component.html',
  styleUrls: ['./list-products.component.css']
})
export class ListProductsComponent implements OnInit {
  products: any[] = [];
  currentPage = 1;
  pageSize = 3;
  query!: string;
  @ViewChild('deleteModal') deleteModal!: ElementRef;
  @ViewChild('cancelBtn') cancelBtn!: ElementRef;
  @ViewChild('deleteBtn') deleteBtn!: ElementRef;
 constructor(private ProductsService:ProductsService,private dialog:MatDialog){}
 ngOnInit(): void {
  this.fetchProduct();
}
deleteProduct(id:any){

this.ProductsService.delProduct(id).subscribe(()=>{
  this.fetchProduct();

})
}
fetchProduct(){
  console.log("oki")
  this.ProductsService.ListProducts(this.currentPage, this.pageSize).subscribe((data)=>{
     
     
    if (Array.isArray(data.results)) {
      this.products = [];
      for (const product of data.results) {

        const createdDate = new Date(product.created_at).toLocaleDateString();
        const updatedDate = new Date(product.updated_at).toLocaleDateString();
        const creatorUsername= product.creator.username
        console.log(creatorUsername)
        const formattedProduct = { product, creatorUsername,createdDate, updatedDate };
        this.products.push(formattedProduct);
        console.log(this.products)
      }
      
}})
}
openAddProductDialog(): void {
  const dialogRef: MatDialogRef<any> = this.dialog.open(AddProductsComponent, {
    width: '400px'
  });

  dialogRef.afterClosed().subscribe(result => {
    // Perform any necessary actions after the dialog is closed
    // if (result) {
      // Handle the result or perform any other logic
      console.log('Serial added:', result);
      this.fetchProduct()
    // }
  });
}
nextPage(): void {
  this.currentPage++;
  console.log(this.currentPage)
  this.fetchProduct();
}
previousPage(): void {
  if (this.currentPage > 1) {
    this.currentPage--;
    console.log(this.currentPage)
    this.fetchProduct();
  }
}
openDeleteDialog(id: any): void {
  const dialogRef: MatDialogRef<any> = this.dialog.open(DeleteDialogProductComponent, {
    width: '400px',
    data: { id }
  });

   dialogRef.afterClosed().subscribe(result => {
    if (result === 'delete') {
      // this.deleteSerial(id);
      this.fetchProduct()
    }
  }); 
}
searchProducts() {
  console.log(this.query)
  this.ProductsService.searchProducts(this.query)
    .subscribe((data: any) => {
      if (Array.isArray(data.results)) {
        this.products = [];
        for (const product of data.results) {
          const createdDate = new Date(product.created_at).toLocaleDateString();
          const updatedDate = new Date(product.updated_at).toLocaleDateString();
          const creatorUsername= product.creator
          console.log(creatorUsername)
          const formattedProduct = { product, creatorUsername,createdDate, updatedDate };
          this.products.push(formattedProduct);

          
        }
        
  }
    });
}
}
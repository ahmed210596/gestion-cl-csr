import { Component } from '@angular/core';
import {  Inject } from '@angular/core';
import { SerialService } from '../serial.service';
import { MatDialogRef, MAT_DIALOG_DATA } from '@angular/material/dialog';
import { Router } from '@angular/router';
@Component({
  selector: 'app-delete-dialog-serial',
  templateUrl: './delete-dialog-serial.component.html',
  styleUrls: ['./delete-dialog-serial.component.css']
})
export class DeleteDialogSerialComponent {
  constructor(
    public dialogRef: MatDialogRef<DeleteDialogSerialComponent>,
    @Inject(MAT_DIALOG_DATA) public data: any,private serialService:SerialService,private router: Router
  ) {}
  confirmDelete(): void {
    console.log(this.data)
    
    this.serialService.delSerial(this.data.id).subscribe(() => {
      this.dialogRef.close(true);   
      
      this.router.navigate(['/list-prod']);
    });
          
      
  }
  }


import { AfterViewInit, Component, ElementRef, OnInit, ViewChild } from '@angular/core';
import { SerialService } from '../serial.service';
import * as M from 'materialize-css';
import { MatDialog, MatDialogRef } from '@angular/material/dialog';
import { AddSerialsComponent } from '../add-serials/add-serials.component';
import { DeleteDialogSerialComponent } from '../delete-dialog-serial/delete-dialog-serial.component';


@Component({
  selector: 'app-list-serials',
  templateUrl: './list-serials.component.html',
  styleUrls: ['./list-serials.component.css']
})
export class ListSerialsComponent implements OnInit {
  serials: any[] = [];
  currentPage = 1;
  pageSize = 3;
  query: string = '';
  @ViewChild('deleteModal') deleteModal!: ElementRef;
  @ViewChild('cancelBtn') cancelBtn!: ElementRef;
  @ViewChild('deleteBtn') deleteBtn!: ElementRef;

  constructor(private serialService: SerialService,private dialog:MatDialog) { }

  /* ngAfterViewInit(): void {
    M.Modal.init(this.deleteModal.nativeElement);
  } */

  ngOnInit(): void {
    this.fetchSerial();
  }

  fetchSerial(): void {
    this.serialService.ListSerials(this.currentPage, this.pageSize).subscribe((data) => {
      if (Array.isArray(data.results)) {
        this.serials = data.results.map((serial: any) => ({
          serial,
          creatorUsername: serial.creator,
          createdDate: new Date(serial.created_at).toLocaleDateString(),
          updatedDate: new Date(serial.updated_at).toLocaleDateString()
        }));
      }
    });
  }

  nextPage(): void {
    this.currentPage++;
    this.fetchSerial();
  }
  openAddSerialDialog(): void {
    const dialogRef: MatDialogRef<any> = this.dialog.open(AddSerialsComponent, {
      width: '400px'
    });
  
    dialogRef.afterClosed().subscribe(result => {
      // Perform any necessary actions after the dialog is closed
      // if (result) {
        // Handle the result or perform any other logic
        console.log('Serial added:', result);
        this.fetchSerial()
      // }
    });
  }

  /* deleteSerial(id: any): void {
    M.Modal.getInstance(this.deleteModal.nativeElement).open();

    this.deleteBtn.nativeElement.onclick = () => {
      this.serialService.delSerial(id).subscribe(() => {
        M.Modal.getInstance(this.deleteModal.nativeElement).close();
        this.fetchSerial();
      });
    };
  } */
  openDeleteDialog(id: any): void {
    const dialogRef: MatDialogRef<any> = this.dialog.open(DeleteDialogSerialComponent, {
      width: '400px',
      data: { id }
    });
  
     dialogRef.afterClosed().subscribe(result => {
      if (result === 'delete') {
        // this.deleteSerial(id);
        this.fetchSerial()
      }
    }); 
  }

 /*  openDeleteModal(): void {
    M.Modal.getInstance(this.deleteModal.nativeElement).open();
  }

  closeDeleteModal(): void {
    M.Modal.getInstance(this.deleteModal.nativeElement).close();
  } */

  previousPage(): void {
    if (this.currentPage > 1) {
      this.currentPage--;
      this.fetchSerial();
    }
  }

  searchSerials(): void {
    this.serialService.searchSerials(this.query).subscribe((data) => {
      if (Array.isArray(data)) {
        this.serials = data.map((serial: any) => ({
          serial,
          creatorUsername: serial.creator,
          createdDate: new Date(serial.created_at).toLocaleDateString(),
          updatedDate: new Date(serial.updated_at).toLocaleDateString()
        }));
      }
    });
  }
}


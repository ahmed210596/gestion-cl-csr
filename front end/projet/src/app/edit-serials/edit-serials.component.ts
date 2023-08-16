import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { SerialService } from '../serial.service';
import { ActivatedRoute, Router } from '@angular/router';
@Component({
  selector: 'app-edit-serials',
  templateUrl: './edit-serials.component.html',
  styleUrls: ['./edit-serials.component.css']
})
export class EditSerialsComponent implements OnInit {
  angForm:FormGroup
  id: any;
  constructor(private fb:FormBuilder,private SerialsService:SerialService,private route: Router,private ActivatedRoute:ActivatedRoute){this.angForm=this.fb.group({
    serial_number:['',Validators.required],
    
    
    
  })}
  ngOnInit(): void {
    this.ActivatedRoute.params.subscribe(paramId =>{
      this.id=paramId['id'];
      this.SerialsService.getSerial(this.id).subscribe(data=>{
        this.angForm?.patchValue(data);
      })
    })
    
  }
  postdata(data:any){
  this.SerialsService.editSerial(this.id,this.angForm?.value).subscribe(data=>{ 
    this.route.navigate(['list-serial']);
  })
  }
}

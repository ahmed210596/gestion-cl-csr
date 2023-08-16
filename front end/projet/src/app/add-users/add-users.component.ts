import { Component ,Input,OnInit} from '@angular/core';
import { FormGroup,FormBuilder, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { DataService } from '../data.service';
@Component({
  selector: 'app-add-users',
  templateUrl: './add-users.component.html',
  styleUrls: ['./add-users.component.css']
})
export class AddUsersComponent implements OnInit {
  angForm!: FormGroup;
  @Input() childData: any;
constructor(private fb:FormBuilder,private DataService:DataService,private route: Router){}
  ngOnInit(): void {
    this.angForm=this.fb.group({
      matricule:['',Validators.required],
      password:['',Validators.required],
      password_confirm:['',Validators.required],
      email:['',Validators.required],
      username:['',Validators.required],
      
      
    });
  }
  postdata(){
    
  this.DataService.addUser(this.angForm.value).subscribe(data=>{ 
    this.route.navigate(['list-users']);
  });
  }
}

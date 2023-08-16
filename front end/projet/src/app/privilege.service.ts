import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Privilege } from './Privilege';

@Injectable({
  providedIn: 'root'
})
export class PrivilegeService {

  APIUrl = "http://127.0.0.1:8000/role";
  
  
  constructor(private http:HttpClient) { }
  ListPrivileges(){
    return this.http.get<Privilege>(this.APIUrl);
  }
  delPrivileges(id:any){
    return this.http.delete<Privilege>(this.APIUrl+'/'+id);
}
addPrivilege(data:any){
  return this.http.post<Privilege>(this.APIUrl+'/',data);
}
editPrivilege(id:number,data:any){
  return this.http.put<Privilege>(this.APIUrl+'/'+id,data);
}
getPrivilege(id:any){
  return this.http.get<Privilege>(this.APIUrl+'/'+id);
}
}

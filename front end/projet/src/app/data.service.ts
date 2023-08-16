import { Injectable } from '@angular/core';
import {HttpClient,HttpParams } from '@angular/common/http';
import { Users } from './users';
import { Observable } from 'rxjs';
@Injectable({
  providedIn: 'root'
})
export class DataService {
   APIUrl = "http://127.0.0.1:8000/user";
   api="http://127.0.0.1:8000/user/search"
  constructor(private http:HttpClient) { }
  ListUsers(page: number, pageSize: number):Observable<any>{
    let params = new HttpParams()
      .set('page', page.toString())
      .set('page_size', pageSize.toString());
    return this.http.get<any>(this.APIUrl,{ params });
  }
  delUser(id:any):Observable<Users>{
    return this.http.delete<Users>(this.APIUrl+'/'+id);
}
addUser(data:any):Observable<Users>{
  return this.http.post<Users>(this.APIUrl+'/',data);
}
editUser(id:number,data:any):Observable<Users>{
  return this.http.put<Users>(this.APIUrl+'/'+id,data);
}
getUser(id:any):Observable<Users>{
  return this.http.get<Users>(this.APIUrl+'/'+id);
}
searchUsers(query: string) {
  const url = `${this.api}?q=${query}`;
  return this.http.get(url);
}
activate(id:any,data:any){
  return this.http.put<Users>(this.APIUrl+'/'+id+'/'+'activate',data);
}
}

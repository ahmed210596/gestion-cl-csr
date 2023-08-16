import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { KeyCSR } from './KeyCSR';
import { Observable } from 'rxjs';
@Injectable({
  providedIn: 'root'
})
export class KeyCSRService {
   API = 'http://127.0.0.1:8000/keycsrs';

  constructor(private http:HttpClient) { }
  listKeys(): Observable<KeyCSR> {
    return this.http.get<KeyCSR>(this.API);
    
  }
 
addkey(data:any){
  return this.http.post<KeyCSR>(this.API+'/',data);
}
editkey(id:any,data:any){
  return this.http.put<KeyCSR>(this.API+'/'+id,data);
}
changestatuskey(id:any,data:any){
  return this.http.put<KeyCSR>(this.API+'/'+id+'/'+'changestatus',data);
}
getkey(id:any){
  return this.http.get<KeyCSR>(this.API+'/'+id);
}
}

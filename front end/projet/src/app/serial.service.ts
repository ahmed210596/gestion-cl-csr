import { HttpClient, HttpParams } from '@angular/common/http';
import { Injectable } from '@angular/core';
import{Serial} from './serial'

@Injectable({
  providedIn: 'root'
})
export class SerialService {
  APIUrl = "http://127.0.0.1:8000/serial";
  api="http://127.0.0.1:8000/serial/search"
  constructor(private http:HttpClient) { }
  ListSerials(page: number, pageSize: number){
    let params = new HttpParams()
    .set('page', page.toString())
    .set('page_size', pageSize.toString());
    return this.http.get<any>(this.APIUrl,{params});
  }
  delSerial(id:any){
    return this.http.delete<Serial>(this.APIUrl+'/'+id);
}
addSerial(data:any){
  return this.http.post<Serial>(this.APIUrl+'/',data);
}
editSerial(id:number,data:any){
  return this.http.put<Serial>(this.APIUrl+'/'+id,data);
}
getSerial(id:any){
  return this.http.get<Serial>(this.APIUrl+'/'+id);
}
searchSerials(query: string) {
  const url = `${this.api}?q=${query}`;
  return this.http.get(url);
}
}

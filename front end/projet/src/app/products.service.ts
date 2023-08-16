import { Injectable } from '@angular/core';
import { Products } from './products';
import { HttpClient, HttpParams } from '@angular/common/http';
import { Observable } from 'rxjs';
@Injectable({
  providedIn: 'root'
})
export class ProductsService {
  APIUrl = "http://127.0.0.1:8000/product";
  api="http://127.0.0.1:8000/product/search"
  
  constructor(private http:HttpClient) { }
  ListProducts(page: number, pageSize: number):Observable<any>{
    let params = new HttpParams()
    .set('page', page.toString())
    .set('page_size', pageSize.toString());
    return this.http.get<any>(this.APIUrl,{params});
  }
  delProduct(id:any):Observable<Products>{
    return this.http.delete<Products>(this.APIUrl+'/'+id);
}
addPoduct(data:any):Observable<Products>{
  return this.http.post<Products>(this.APIUrl+'/',data);
}
editProduct(id:number,data:any):Observable<Products>{
  
  return this.http.put<Products>(this.APIUrl+'/'+id,data);
}
getProduct(id:any):Observable<Products>{
  return this.http.get<Products>(this.APIUrl+'/'+id);
}
searchProducts(query: string) {
  const url = `${this.api}?q=${query}`;
  return this.http.get(url);
}
}

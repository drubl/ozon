import { ProductCard } from './../ProductCard';
import { Injectable } from '@angular/core';
import { HttpClient, HttpParams } from '@angular/common/http';
import { Observable } from 'rxjs';

export class Products {
  products: ProductCard[]
}

@Injectable({
  providedIn: 'root'
})


export class ProductService {
  constructor(private http: HttpClient) { }
  searchProduct(event): Observable<Products> {
    return this.http.get<Products>('/api/products', {
      params: new HttpParams().set('search', event)
    });
  }


  getProductItem(id): Observable<ProductCard> {
    return this.http.get<ProductCard>(`/api/products/${id}`);
  }
}


import { Product } from './product';
import {Injectable} from '@angular/core';
import { Observable, of } from 'rxjs';
import { HttpClient } from '@angular/common/http';
import {map} from 'rxjs/operators';


export class Cart {
  purchase: number[];
  totalPrice?: number;
  totalWeight?: number;
  countPurchase?: number;
}

export class SearchProducts {
  products: Product[];
}

@Injectable({
  providedIn: 'root'
})
export class ProductService {
  private productsUrl = '/api/products/';
  public PRODUCTS: Product[];
  constructor(private http: HttpClient) { }
  searchProducts(title: string): Observable<Product[]> {
    if (!title.trim()) {
      return of([]);
    }
    return this.http.get<SearchProducts>(`${this.productsUrl}?search=${title}`).pipe(map(searchProducts => searchProducts.products));
  }
  getProduct(id: string): Observable<Product> {
    return this.http.get<Product>(`${this.productsUrl}/${id}`);
  }
}

import { Product } from '../../../product';
import {Injectable} from '@angular/core';
import {from, Observable, of} from 'rxjs';
import {HttpClient, HttpHeaders} from '@angular/common/http';
import {map} from 'rxjs/operators';
import {CookieService} from 'ngx-cookie-service';


export class SearchProducts {
  products: Product[];
}

@Injectable({
  providedIn: 'root'
})
export class ProductService {
  private productsUrl = '/api/products/';
  private token = this.cookieService.get('csrftoken');
  constructor(private http: HttpClient, private cookieService: CookieService) { }
  searchProducts(title: string): Observable<Product[]> {
    return this.http.get<SearchProducts>(`${this.productsUrl}?search=${title}`).pipe(map(searchProducts => searchProducts.products));
  }
  getProduct(id: string): Observable<Product> {
    return this.http.get<Product>(`${this.productsUrl}/${id}`);
  }
  addProduct(id: number) {
    return this.http.post(`/api/customer/cart/${id}/`, {}, {
      headers: new HttpHeaders({
        'X-CSRFToken': this.token
      })
    });
  }
  deleteProduct(id: number) {
    return this.http.delete(`/api/customer/cart/${id}/`, {
      headers: new HttpHeaders({
        'X-CSRFToken': this.token
      })
    });
  }
}

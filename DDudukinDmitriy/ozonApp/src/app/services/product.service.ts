import {ProductCard} from './../ProductCard';
import {Injectable} from '@angular/core';
import {HttpClient, HttpHeaders, HttpParams} from '@angular/common/http';
import {Observable} from 'rxjs';
import {CookieService} from "ngx-cookie-service";
import {Categories} from "../Categories";

export class Products {
  products: ProductCard[]
}
export class CategoriesArray{
  categories: Categories[]
}

@Injectable({
  providedIn: 'root'
})


export class ProductService {
  public token = this.cookieService.get('csrftoken')
  public headersToken = new HttpHeaders({
    'X-CSRFToken': this.token
  })

  constructor(private http: HttpClient, private cookieService: CookieService) {
  }

  getAllProducts(): Observable<Products> {
    return this.http.get<Products>('/api/products')
  }

  getCategories():Observable<CategoriesArray>{
    return this.http.get<CategoriesArray>('/api/categories')
  }

  searchProduct(event): Observable<Products> {
    return this.http.get<Products>('/api/products', {
      params: new HttpParams().set('search', event)
    });
  }

  getProductItem(id): Observable<ProductCard> {
    return this.http.get<ProductCard>(`/api/products/${id}`);
  }

  addItemToCart(id) {
    this.http.post(`api/customer/cart/${id}/`, {}, {
      headers: this.headersToken
    })
      .subscribe()
  }

  getCategoryProducts(category): Observable<ProductCard>{
    return this.http.get<ProductCard>(`/api/category/${category}`)
  }

  deleteProductItem(id) {
    this.http.delete(`/api/customer/cart/${id}/`, {
      headers: this.headersToken
    }).subscribe()
  }
}


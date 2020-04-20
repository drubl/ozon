import { Injectable } from '@angular/core';
import {Auth} from "./auth";
import {Product, Products} from "./product";
import {HttpClient} from "@angular/common/http";
import {Observable} from "rxjs";
import {Cart} from './cart';



@Injectable({
  providedIn: 'root'
})
export class CartService {
  private auth: Auth;
  constructor(auth: Auth, private http: HttpClient) {
  }
  getProductsCart(): Observable<Cart> {
    return this.http.get<Cart>(`/api/customer/cart/`);
  }
}

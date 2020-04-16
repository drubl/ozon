import { Injectable } from '@angular/core';
import {Auth} from "./auth";
import {Product, Products} from "./product";
import {HttpClient} from "@angular/common/http";
import {Observable} from "rxjs";
import {Cart} from "./product.service";



@Injectable({
  providedIn: 'root'
})
export class CardService {
  private auth: Auth;
  constructor(auth: Auth, private http: HttpClient) {
  }
  getProductsCart(id: number): Observable<Cart> {
    console.log('id in carService', id);
    return this.http.get<Cart>(`/api/customer/${id}/cart/`);
  }
}

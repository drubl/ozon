import { Injectable } from '@angular/core';
import {Auth} from "./auth";
import {Product} from "./product";
import {HttpClient} from "@angular/common/http";
import {Observable} from "rxjs";

export class CartProducts {
  purchase: any;
  totalPrice: number;
  totalWeight: any;
  countPurchase: string | number;
}


@Injectable({
  providedIn: 'root'
})
export class CardService {
  public cartProductsUrl = `/api/customer/1/cart/`;
  private http: HttpClient;

  constructor(private auth: Auth, http: HttpClient) {
  }
}

import { Injectable } from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {Observable} from "rxjs";
import {UsersCart} from "../UsersCart";

export class UserCartProduct{
  purchase: UsersCart[]
}
@Injectable({
  providedIn: 'root'
})
export class CartService {
  constructor(private http:HttpClient) { }
  getUserCart():Observable<UserCartProduct>{
    return this.http.get<UserCartProduct>('/api/customer/1/cart/')
  }
}

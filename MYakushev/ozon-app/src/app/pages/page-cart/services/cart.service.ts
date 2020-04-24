import {Injectable} from '@angular/core';
import {AuthService} from '../../../core/auth/auth.service';
import {Product, Products} from '../../../product';
import {HttpClient} from '@angular/common/http';
import {Observable} from 'rxjs';

export class Cart {
  countProducts: number;
  id: number;
  is_checkout: boolean;
  purchase: Products[];
  totalPrice: number;
  totalWeight: number;
}

@Injectable({
  providedIn: 'root'
})
export class CartService {
  private auth: AuthService;

  constructor(auth: AuthService, private http: HttpClient) {
  }

  getProductsCart(): Observable<Cart> {
    return this.http.get<Cart>(`/api/customer/cart/`);
  }
}

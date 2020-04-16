import { Product } from './product';
import { PRODUCTS} from './mock-base-products';
import {Injectable} from '@angular/core';
import { Observable, of } from 'rxjs';


export class Cart {
  purchase: number[];
  totalPrice?: number;
  totalWeight?: number;
  countPurchase?: number;
}

@Injectable({
  providedIn: 'root'
})
export class ProductService {
  public productsCart: [];
  private cart: Observable<Cart> = of({purchase: [1, 2]}, {purchase: [1, 2]});
  constructor() { }
  addProductToCart(product): any {
    this.productsCart.push(product);
  }
  getProducts(): Observable<Product[]> {
    return of(PRODUCTS);
  }
  getCart(): Observable<Cart> {
    return of({purchase: [1, 1]} as Cart);
  }
}

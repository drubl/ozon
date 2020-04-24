import {Component, EventEmitter, OnInit, Output} from '@angular/core';
import {ProductService} from '../page-product/services/product.service';
import {CartService} from './services/cart.service';
import {HttpClient} from '@angular/common/http';
import {AuthService} from '../../core/auth/auth.service';
import {Cart} from './services/cart.service';
import {Product, Products} from '../../product';


@Component({
  selector: 'app-page-cart',
  templateUrl: './page-cart.component.html',
  styleUrls: ['./page-cart.component.css']
})


export class PageCartComponent implements OnInit {
  constructor(public productService: ProductService, private cardService: CartService, private http: HttpClient, private auth: AuthService) {
  }

  cart: Cart;
  productsCartInfo: Products[];

  ngOnInit(): void {
    this.getCart();
  }

  getCart() {
    this.cardService.getProductsCart().subscribe(cart => {
      this.cart = cart;
      this.productsCartInfo = this.cart.purchase;
      console.log('cart', this.cart);
      console.log('cartInfo', this.productsCartInfo);
    });
  }
}

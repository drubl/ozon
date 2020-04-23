import {Component, EventEmitter, OnInit, Output} from '@angular/core';
import {ProductService} from '../product.service';
import {CartService} from '../cart.service';
import {HttpClient} from '@angular/common/http';
import {Auth} from '../auth';
import {Cart} from '../cart';
import {Product, Products} from '../product';


@Component({
  selector: 'app-page-cart',
  templateUrl: './page-cart.component.html',
  styleUrls: ['./page-cart.component.css']
})


export class PageCartComponent implements OnInit {
  constructor(public productService: ProductService, private cardService: CartService, private http: HttpClient, private auth: Auth) {
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

  refreshCart() {
    console.log('Получилось');
  }
}

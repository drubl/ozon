import {Component, OnInit} from '@angular/core';
import {ProductService} from '../product.service';
import {CardService} from "../card.service";
import {HttpClient} from "@angular/common/http";
import {Auth} from "../auth";
import {Cart} from "../cart";
import {Product, Products} from "../product";


@Component({
  selector: 'app-page-cart',
  templateUrl: './page-cart.component.html',
  styleUrls: ['./page-cart.component.css']
})


export class PageCartComponent implements OnInit {

  constructor(public productService: ProductService, private cardService: CardService, private http: HttpClient, private auth: Auth) {
  }
  cart: Cart;
  productsCartInfo: Products[];
  // productsCart: Product[];

  ngOnInit(): void {
    this.getCart(this.auth.id);
  }

  getCart(id) {
    if (!id) {
      console.log('Пользователь не вошел');
    } else {
      this.cardService.getProductsCart(id).subscribe(cart => {
          this.cart = cart;
          this.productsCartInfo = this.cart.purchase;
          // this.productsCart = this.productsCartInfo;
          console.log('cart', this.cart);
          console.log('cartInfo', this.productsCartInfo);
          // console.log('cart', this.productsCart);
      });
    }
  }
}

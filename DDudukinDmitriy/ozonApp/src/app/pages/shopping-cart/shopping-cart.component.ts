import {Component, Input, OnInit,} from '@angular/core';

import {ProductCardComponent} from '../../product-card/product-card.component'
import {CartService} from "../../services/cart.service";
import {CheckOutData, UsersCart} from "../../UsersCart";
import {ProductService} from "../../services/product.service";

@Component({
  selector: 'app-shopping-cart',
  templateUrl: './shopping-cart.component.html',
  styleUrls: ['./shopping-cart.component.css']
})
export class ShoppingCartComponent implements OnInit {
  isActive: boolean = false;
  checkOut: CheckOutData;
  userCartProducts: UsersCart[];

  constructor(private cartService: CartService,
              private productService: ProductService) {
  }

  ngOnInit(): void {
    this.getCart();
  }

  getCart() {
    this.cartService.getCheckOutData()
      .subscribe(checkOut => {
        this.checkOut = checkOut;
        this.userCartProducts = checkOut.purchase
      })
  }

  deleteProductFromCart(id) {
    this.productService.deleteProductItem(id)
  }

  checkAll() {
    this.isActive = !this.isActive;
  }
}

import { Component, OnInit } from '@angular/core';

import { ProductCardComponent } from '../product-card/product-card.component'
import {CartService} from "../services/cart.service";
import {UsersCart} from "../UsersCart";
@Component({
  selector: 'app-shopping-cart',
  templateUrl: './shopping-cart.component.html',
  styleUrls: ['./shopping-cart.component.css']
})
export class ShoppingCartComponent implements OnInit {

userCartProducts:UsersCart[];
  constructor(private cartService: CartService) { }

  ngOnInit(): void {
    this.getCart()
  }
  getCart(){
    this.cartService.getUserCart()
      .subscribe(cart => {
        this.userCartProducts = cart.purchase;
        console.log(cart.purchase)
      })
  }
}

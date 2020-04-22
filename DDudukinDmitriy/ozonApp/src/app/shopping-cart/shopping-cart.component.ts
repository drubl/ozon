import {Component, Input, OnInit,} from '@angular/core';

import { ProductCardComponent } from '../product-card/product-card.component'
import {CartService} from "../services/cart.service";
import {CheckOutData, UsersCart} from "../UsersCart";
@Component({
  selector: 'app-shopping-cart',
  templateUrl: './shopping-cart.component.html',
  styleUrls: ['./shopping-cart.component.css']
})
export class ShoppingCartComponent implements OnInit {
  isActive:boolean = false;
  checkOut: CheckOutData;
  userCartProducts: UsersCart[];

  constructor(private cartService: CartService) {
  }

  ngOnInit(): void {
    this.getCheckOutData();
    this.getCart()
  }

  getCart() {
    this.cartService.getUserCart()
      .subscribe(cart => {
        this.userCartProducts = cart.purchase;
      })
  }

  getCheckOutData() {
    this.cartService.getCheckOutData()
      .subscribe(checkOut => {
        this.checkOut = checkOut;
      })
  }
  checkAll(){
    this.isActive = !this.isActive;
  }
}

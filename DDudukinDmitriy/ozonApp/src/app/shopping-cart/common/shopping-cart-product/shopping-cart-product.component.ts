import {Component, Input, OnInit} from '@angular/core';
import { ProductCard } from '../../../ProductCard'
import {UsersCart} from "../../../UsersCart";
@Component({
  selector: 'app-shopping-cart-product',
  templateUrl: './shopping-cart-product.component.html',
  styleUrls: ['./shopping-cart-product.component.css']
})
export class ShoppingCartProductComponent implements OnInit {
  @Input() shoppingCartProduct: UsersCart;
  constructor() { }

  ngOnInit(): void {
  }

}

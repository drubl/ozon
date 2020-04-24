import {Component, EventEmitter, Input, OnInit, Output} from '@angular/core';
import {UsersCart} from "../../../../UsersCart";

@Component({
  selector: 'app-shopping-cart-product',
  templateUrl: './shopping-cart-product.component.html',
  styleUrls: ['./shopping-cart-product.component.css']
})
export class ShoppingCartProductComponent implements OnInit {
  @Input() shoppingCartProduct: UsersCart;
  @Output() onDeleteProductItem: EventEmitter<any> = new EventEmitter<any>()

  constructor() {
  }

  ngOnInit(): void {
  }

  deleteProductItem(id) {
    this.onDeleteProductItem.emit(id);
  }
}

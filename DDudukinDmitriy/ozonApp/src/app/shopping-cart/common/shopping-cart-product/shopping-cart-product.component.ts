import {Component, Input, OnInit} from '@angular/core';
import { ProductCard } from '../../../ProductCard'
import {UsersCart} from "../../../UsersCart";
import {ProductService} from "../../../services/product.service";
import {CartService} from "../../../services/cart.service";
@Component({
  selector: 'app-shopping-cart-product',
  templateUrl: './shopping-cart-product.component.html',
  styleUrls: ['./shopping-cart-product.component.css']
})
export class ShoppingCartProductComponent implements OnInit {
  @Input() shoppingCartProduct: UsersCart;
  constructor(private productService: ProductService,
              private cartService: CartService) { }

  ngOnInit(): void {
  }
  deleteProductItem(id){
    this.productService.deleteProductItem(id);
  }
}

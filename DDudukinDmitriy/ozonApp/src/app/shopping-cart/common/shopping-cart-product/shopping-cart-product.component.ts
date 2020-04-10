import { Component, OnInit } from '@angular/core';
import { ProductCard } from '../../../ProductCard'
import { PRODUCTCARD } from '../../../mock-product-card'

@Component({
  selector: 'app-shopping-cart-product',
  templateUrl: './shopping-cart-product.component.html',
  styleUrls: ['./shopping-cart-product.component.css']
})
export class ShoppingCartProductComponent implements OnInit {
  public Addedproduct: ProductCard[] = PRODUCTCARD;
  constructor() { }

  ngOnInit(): void {
  }

}

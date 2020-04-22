import { ProductCard } from './../ProductCard';
import { Component, OnInit, Input, Output, EventEmitter } from '@angular/core';
import {UserService} from "../services/user.service";
import {ProductService} from "../services/product.service";

@Component({
  selector: 'app-product-card',
  templateUrl: './product-card.component.html',
  styleUrls: ['./product-card.component.css']
})


export class ProductCardComponent implements OnInit {
  @Input() product: ProductCard;

  productItem: ProductCard;

  constructor(private productService: ProductService) { }
  ngOnInit(): void {
  }
  public addToCartHandler(id) {
    this.productService.addItemToCart(id)
  }
}

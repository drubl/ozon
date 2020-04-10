import { Component, OnInit, Output, EventEmitter } from '@angular/core';
import { ProductCard } from '../ProductCard'
import { PRODUCTCARD } from '../mock-product-card'

@Component({
  selector: 'app-product-card',
  templateUrl: './product-card.component.html',
  styleUrls: ['./product-card.component.css']
})
export class ProductCardComponent implements OnInit {
  @Output() onAdd: EventEmitter<ProductCard> = new EventEmitter<ProductCard>()

  addedProductToCard: ProductCard;
  public productCard: ProductCard[] = PRODUCTCARD;
  constructor() { }

  ngOnInit(): void {
  }
  addToCart(product: ProductCard): void {
    this.addedProductToCard = product;
    console.log(this.addedProductToCard);

  }
}

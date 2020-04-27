import { ProductCard } from './../ProductCard';
import { Component, OnInit, Input, Output, EventEmitter } from '@angular/core';
@Component({
  selector: 'app-product-card',
  templateUrl: './product-card.component.html',
  styleUrls: ['./product-card.component.css']
})


export class ProductCardComponent implements OnInit {
  @Output() onAddToCard: EventEmitter<any> = new EventEmitter<any>();
  @Input() product: ProductCard;


  constructor() { }
  ngOnInit(): void {
  }
  public addToCart(id) {
    this.onAddToCard.emit(id)
  }
}

import {Component, EventEmitter, Input, Output} from '@angular/core';
import {Product} from '../../../product';


@Component({
  selector: 'app-product-item',
  templateUrl: './product-item.component.html',
  styleUrls: ['./product-item.component.css']
})
export class ProductItemComponent {
  @Output() EventClickAddToCart: EventEmitter<any> = new EventEmitter<any>();
  @Input() productItem: Product;

  clickButtonAddToCart(id) {
    this.EventClickAddToCart.emit(id);
  }
}

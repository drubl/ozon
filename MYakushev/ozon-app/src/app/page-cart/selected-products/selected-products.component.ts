import {Component, EventEmitter, Input, OnInit, Output} from '@angular/core';
import {Cart} from '../../cart';
import {ProductService} from '../../product.service';
import {PageCartComponent} from '../page-cart.component';
import {CartService} from '../../cart.service';

@Component({
  selector: 'app-selected-products',
  templateUrl: './selected-products.component.html',
  styleUrls: ['./selected-products.component.css']
})
export class SelectedProductsComponent implements OnInit {
  @Output() refreshCart: EventEmitter<string> = new EventEmitter<string>();
  @Input() cart: Cart;
  constructor(private productService: ProductService, private pageCartComponent: PageCartComponent, private cardService: CartService) { }
  ngOnInit(): void {
  }
  deleteToCart(id: number) {
    console.log(id);
    this.productService.deleteProduct(id).subscribe(answer => {
      console.log('answer', answer);
    });
  }
}

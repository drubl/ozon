import {Component, Input, OnInit} from '@angular/core';
import {Cart} from '../../cart';

@Component({
  selector: 'app-information-products',
  templateUrl: './information-products.component.html',
  styleUrls: ['./information-products.component.css']
})
export class InformationProductsComponent implements OnInit {
  @Input() cart: Cart;
  constructor() { }
  ngOnInit(): void {
  }

}

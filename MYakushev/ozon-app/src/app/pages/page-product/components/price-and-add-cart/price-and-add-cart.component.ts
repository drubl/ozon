import {Component, Input, OnInit} from '@angular/core';

@Component({
  selector: 'app-price-and-add-cart',
  templateUrl: './price-and-add-cart.component.html',
  styleUrls: ['./price-and-add-cart.component.css']
})
export class PriceAndAddCartComponent implements OnInit {
  @Input() productPrice;
  constructor() { }

  ngOnInit(): void {
  }

}

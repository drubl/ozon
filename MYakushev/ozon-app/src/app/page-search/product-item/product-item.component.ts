import {Component, Input, OnInit, Output} from '@angular/core';
import {Product} from "../../product";



@Component({
  selector: 'app-product-item',
  templateUrl: './product-item.component.html',
  styleUrls: ['./product-item.component.css']
})
export class ProductItemComponent implements OnInit {
  @Input() productItem: Product;
  constructor() { }

  ngOnInit(): void {
  }

}

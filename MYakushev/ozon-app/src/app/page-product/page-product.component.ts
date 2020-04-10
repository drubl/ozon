import { Component, OnInit } from '@angular/core';
import { Product } from '../product';
import { PRODUCTS } from '../mock-base-products';

@Component({
  selector: 'app-page-product',
  templateUrl: './page-product.component.html',
  styleUrls: ['./page-product.component.css']
})
export class PageProductComponent implements OnInit {
  public products = PRODUCTS;
  constructor() { }

  ngOnInit(): void {
  }

}

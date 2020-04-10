import { Component, OnInit } from '@angular/core';
import { Product } from '../product';
import { PRODUCTS } from '../mock-base-products';

@Component({
  selector: 'app-page-main',
  templateUrl: './page-main.component.html',
  styleUrls: ['./page-main.component.css']
})
export class PageMainComponent implements OnInit {
  public products = PRODUCTS;
  constructor() { }

  ngOnInit(): void {
  }
  info() {
    console.log(this);
  }
}

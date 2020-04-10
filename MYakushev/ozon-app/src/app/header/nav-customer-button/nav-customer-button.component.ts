import { Component, OnInit } from '@angular/core';
import {Cart, ProductService} from '../../product.service';
import {Observable, of} from 'rxjs';

@Component({
  selector: 'app-nav-customer-button',
  templateUrl: './nav-customer-button.component.html',
  styleUrls: ['./nav-customer-button.component.css']
})
export class NavCustomerButtonComponent implements OnInit {
  constructor(private productService: ProductService) {
  }
  public productCartSum = this.productService.productsCart;
  ngOnInit(): void {
  }

}

import { Component, OnInit } from '@angular/core';
import {Cart, ProductService} from '../../product.service';
import {Observable, of} from 'rxjs';
import {Auth} from "../../auth";

@Component({
  selector: 'app-nav-customer-button',
  templateUrl: './nav-customer-button.component.html',
  styleUrls: ['./nav-customer-button.component.css']
})
export class NavCustomerButtonComponent implements OnInit {
  toggleModal = true;
  constructor(private productService: ProductService, public auth: Auth) {
  }
  ngOnInit(): void {
  }

}

import { Component, OnInit, Input } from '@angular/core';
import {ProductService} from "../product.service";
import {Product} from "../product";
import {Observable} from "rxjs";

import { ActivatedRoute } from '@angular/router';
import { Location } from '@angular/common';

@Component({
  selector: 'app-page-product',
  templateUrl: './page-product.component.html',
  styleUrls: ['./page-product.component.css']
})
export class PageProductComponent implements OnInit {
  constructor(private productService: ProductService, private route: ActivatedRoute,
  private location: Location) { }
  product: Product;
  id;
  ngOnInit(): void {
    this.id = this.route.snapshot.paramMap.get(' id').replace(/\D+/g, '');
    this.showSingleProduct(this.id);
  }
  showSingleProduct(id) {
    this.productService.getProduct(id).subscribe(product => {
      this.product = product;
    });
  }
}

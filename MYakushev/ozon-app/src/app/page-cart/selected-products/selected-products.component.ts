import {Component, Input, OnInit} from '@angular/core';
import {ProductService} from '../../product.service';
import {Cart} from "../../cart";
import {Product, Products} from "../../product";

@Component({
  selector: 'app-selected-products',
  templateUrl: './selected-products.component.html',
  styleUrls: ['./selected-products.component.css']
})
export class SelectedProductsComponent implements OnInit {
  @Input() productsCartInfo: Products[];
  constructor(private productService: ProductService) { }
  ngOnInit(): void {
  }
}

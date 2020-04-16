import { Component, OnInit } from '@angular/core';
import { ProductService } from '../../product.service';

@Component({
  selector: 'app-selected-products',
  templateUrl: './selected-products.component.html',
  styleUrls: ['./selected-products.component.css']
})
export class SelectedProductsComponent implements OnInit {

  constructor(private productService: ProductService) { }
  public productCartSum = this.productService.productsCart;
  ngOnInit(): void {
    console.log(this.productService.productsCart);
  }
  info(): void {
    console.log('177777');
  }

}

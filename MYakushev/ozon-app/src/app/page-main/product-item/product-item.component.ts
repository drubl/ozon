import { Component, OnInit } from '@angular/core';
import { Product } from '../../product';
import { PRODUCTS } from '../../mock-base-products';
import { ProductService } from '../../product.service';

@Component({
  selector: 'app-product-item',
  templateUrl: './product-item.component.html',
  styleUrls: ['./product-item.component.css']
})
export class ProductItemComponent implements OnInit {
  public products: Product[] = PRODUCTS;

  constructor(private productService: ProductService) { }

  ngOnInit(): void {
  }
  addProduct(product) {
    this.productService.addProductCart(product);
    console.log(this.productService.productsCart);
  }
}

import { ProductService } from './../services/product.service';
import { ProductCard } from './../ProductCard';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-search-page',
  templateUrl: './search-page.component.html',
  styleUrls: ['./search-page.component.css']
})
export class SearchPageComponent implements OnInit {
  products: ProductCard[];
  addedProductsToCart: ProductCard[];

  constructor(private productService: ProductService) { }

  ngOnInit(): void {
  }
  public searchHandler(event: any) {
    this.productService.searchProduct(event)
      .subscribe(products => {
        this.products = products.products;
      });
  }



  public addToCartHandler(event) {
    console.log(event);
  }
}

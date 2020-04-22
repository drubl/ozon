import { ProductService } from './../services/product.service';
import { ProductCard } from './../ProductCard';
import { Component, OnInit } from '@angular/core';
import {ActivatedRoute, Params} from "@angular/router";

@Component({
  selector: 'app-search-page',
  templateUrl: './search-page.component.html',
  styleUrls: ['./search-page.component.css']
})
export class SearchPageComponent implements OnInit {
  products: ProductCard[];
  inputQueryParam: string;
  addedProductsToCart: ProductCard[];

  constructor(private productService: ProductService,
              private route: ActivatedRoute) { }

  ngOnInit(): void {
    this.route.queryParams.subscribe((params:Params)=>{
      this.inputQueryParam = params.search;
    })
    this.searchHandler(this.inputQueryParam)
  }

  public searchHandler(event: any) {
    this.productService.searchProduct(event)
      .subscribe(products => {
        this.products = products.products;
      });
  }
  public addToCartHandler(event) {
  }
}

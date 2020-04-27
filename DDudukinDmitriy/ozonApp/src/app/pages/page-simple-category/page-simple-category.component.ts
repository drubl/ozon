import { Component, OnInit } from '@angular/core';
import {ProductService} from "../../services/product.service";
import {ActivatedRoute, Params} from "@angular/router";

@Component({
  selector: 'app-page-simple-category',
  templateUrl: './page-simple-category.component.html',
  styleUrls: ['./page-simple-category.component.css']
})
export class PageSimpleCategoryComponent implements OnInit {
public categoryProducts
  constructor(private productService: ProductService,
              private route: ActivatedRoute) { }

  ngOnInit(): void {
  this.getCategoryProducts()
      }
  getCategoryProducts(){
  const category = this.route.snapshot.paramMap.get('category')
    this.productService.getCategoryProducts(category).subscribe(products => {
      this.categoryProducts = products['products'];
      this.getCategoryProducts()
    })
  }
}

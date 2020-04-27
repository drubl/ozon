import { Component, OnInit } from '@angular/core';
import {CategoriesArray, ProductService} from "../../services/product.service";
import {ProductCard} from "../../ProductCard";
import {Categories} from "../../Categories";

@Component({
  selector: 'app-home-page',
  templateUrl: './home-page.component.html',
  styleUrls: ['./home-page.component.css']
})
export class HomePageComponent implements OnInit {
  public products: ProductCard[];

  constructor(private productService: ProductService) { }

  ngOnInit(): void {
    this.getProducts()
  }
  getProducts(){
    this.productService.getAllProducts().subscribe(product =>{
      this.products = product.products
    })
  }
}

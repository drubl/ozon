import { Component, OnInit } from '@angular/core';
import {ProductCard} from "../../../../ProductCard";
import {ProductService} from "../../../../services/product.service";
import {Categories} from "../../../../Categories";

@Component({
  selector: 'app-modal-category',
  templateUrl: './modal-category.component.html',
  styleUrls: ['./modal-category.component.css']
})
export class ModalCategoryComponent implements OnInit {
public categories: Categories[];
  constructor(private productService: ProductService) { }

  ngOnInit(): void {
    this.getCategories();
  }
  getCategories(){
    this.productService.getCategories().subscribe(categories =>{
      this.categories = categories.categories;
      console.log(this.categories)
    })
  }
}

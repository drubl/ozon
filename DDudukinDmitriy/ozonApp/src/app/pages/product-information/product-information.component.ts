import { ProductCard } from '../../ProductCard';
import {Component, Input, OnInit} from '@angular/core';
import {ActivatedRoute} from "@angular/router";
import {ProductService} from "../../services/product.service";
import {Location} from "@angular/common";


@Component({
  selector: 'app-product-information',
  templateUrl: './product-information.component.html',
  styleUrls: ['./product-information.component.css']
})
export class ProductInformationComponent implements OnInit {
  productItemInformation: ProductCard;

  constructor(
    private  route: ActivatedRoute,
    private productService:ProductService,
    private location: Location
  ) { }

  ngOnInit(): void {
    this.getProductInformation();
  }
public getProductInformation(){
    const id = +this.route.snapshot.paramMap.get('id');
    this.productService.getProductItem(id)
      .subscribe(productItem => {
        this.productItemInformation = productItem;
      })
  }
  addToCart(id){
    this.productService.addItemToCart(id);
  }
}

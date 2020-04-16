import { Component, OnInit } from '@angular/core';
import {ProductService, SearchProducts} from '../product.service';
import {CardService} from "../card.service";
import {HttpClient} from "@angular/common/http";
import {Observable, of} from "rxjs";

// export class ProductsCart {
//   id: number;
//   firstPhoto: string;
//   title: string;
//   price: string | number;
//   singleLink: string;
//   description: string;
// }

@Component({
  selector: 'app-page-cart',
  templateUrl: './page-cart.component.html',
  styleUrls: ['./page-cart.component.css']
})



export class PageCartComponent implements OnInit {

  constructor(public productService: ProductService, private cardService: CardService, private http: HttpClient) {
  }

  ngOnInit(): void {
    // this.getProductsCart();
  }

  getProductsCart() {
    // const products = this.http.get('/api/customer/1/cart/');
    // console.log(products);
  }
}

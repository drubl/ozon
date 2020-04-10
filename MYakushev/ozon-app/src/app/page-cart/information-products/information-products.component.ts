import { Component, OnInit } from '@angular/core';
import { ProductService } from '../../product.service';

@Component({
  selector: 'app-information-products',
  templateUrl: './information-products.component.html',
  styleUrls: ['./information-products.component.css']
})
export class InformationProductsComponent implements OnInit {
  public result: any;
  constructor(public  productService: ProductService) { }
  ngOnInit(): void {
  }

}

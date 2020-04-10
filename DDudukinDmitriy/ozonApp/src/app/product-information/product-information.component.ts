import { Component, OnInit } from '@angular/core';
import { ProductCard } from '../ProductCard'
import { PRODUCTCARD } from '../mock-product-card'

@Component({
  selector: 'app-product-information',
  templateUrl: './product-information.component.html',
  styleUrls: ['./product-information.component.css']
})
export class ProductInformationComponent implements OnInit {
  constructor() { }

  ngOnInit(): void {
  }

}

import {Component, EventEmitter, Input, OnInit, Output} from '@angular/core';
import {Product} from "../../product";
import {ProductService} from '../../product.service';
import {NavCustomerButtonComponent} from '../../header/nav-customer-button/nav-customer-button.component';



@Component({
  selector: 'app-product-item',
  templateUrl: './product-item.component.html',
  styleUrls: ['./product-item.component.css']
})
export class ProductItemComponent implements OnInit {
  @Output() cartChange: EventEmitter<string> = new EventEmitter<string>();
  @Input() productItem: Product;
  constructor(private productService: ProductService) { }

  ngOnInit(): void {
  }


  addToCart(id: number) {
    this.productService.addProduct(id).subscribe(answer => {
      console.log(answer);
      this.cartChange.emit();
    });

  }
}
